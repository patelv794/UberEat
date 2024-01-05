
import csv
import json
from time import sleep
import requests

CSV_FILE_NAME = "Breakfast (Cereal, Granola & Oatmeal)"
url = "https://www.ubereats.com/store/fort-green-food-market-beer-%26-grocery-186-dekalb-avenue/Gl7emTw4X5qYPy3IxRmIuw/1a5ede99-3c38-5f9a-983f-2dc8c51988bb/d488b396-a7e7-4989-9e90-beb7cc1d6993?diningMode=DELIVERY&ps=1&scats=d488b396-a7e7-4989-9e90-beb7cc1d6993&scatsectypes=MENU&scatsubs="
href_url = url.split('/')
store_id = href_url[-2]
category_uuuid = href_url[-1].split('?')[0]

cookies = {

    'jwt-session': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE3MDEzODE3ODcyOTQsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiJkODg3OGJkNy1hNTkxLTQwMWQtYTVhOS1mZjU0MmIwMDNkODUiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNzAxMjk1MjY2Mjk0fSwiaWF0IjoxNzAxMjk1MjY2LCJleHAiOjE3MDEzODE2NjZ9.klHfiiT6wqhgrZ10TM_AK70DCUGjDl4OIcu68YgYNWQ',
}

headers = {
    'Host': 'www.ubereats.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'X-Csrf-Token': 'x',
    'Origin': 'https://www.ubereats.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

all_category_name_With_UUID = {}

json_data_category = {
    'storeUuid': f'{store_id}',
    'sfNuggetCount': 50,
    'cbType': 'EATER_ENDORSED',
}
response_category = requests.post(
    'https://www.ubereats.com/_p/api/getStoreV1',
    headers=headers,
    cookies=cookies,
    json=json_data_category,
)

data = json.loads(response_category.text)
raw_data = data['data']['catalogSectionsMap'][f'{store_id}']

for all_raw_data in raw_data:
    catalogSectionUUID = all_raw_data['catalogSectionUUID']
    category_name = all_raw_data['payload']['standardItemsPayload']['title']['text']
    # print(category_name)
    all_category_name_With_UUID[catalogSectionUUID] = category_name

stop_data = True
item_page = 0
count_item = 0
sub_category = {}
while stop_data:

    category_id = [f"{category_uuuid}"]
    json_data = {
        'storeFilters': {
            'storeUuid': f'{store_id}',
            'sectionUuids': category_id,
            'subsectionUuids': None,
            'sectionTypes': [
                'MENU',
            ],
            'shouldReturnSegmentedControlData': True,
        },
        'pagingInfo': {
            'enabled': True,
            'offset': item_page,
        },
    }

    response = requests.post(
        'https://www.ubereats.com/_p/api/getCatalogPresentationV2',
        headers=headers,
        cookies=cookies,
        json=json_data,
    )
    print(response.status_code)
    data = json.loads(response.text)

    if not sub_category:
        for get_subCat in data['data']['catalog']:
            uuid = get_subCat['catalogSectionUUID']
            name = get_subCat['payload']['standardItemsPayload']['title']['text']
            sub_category[uuid] = name
            # sub_category['cat_uuid'] = uuid

    for dat in data['data']['catalog'][0]['payload']['standardItemsPayload']['catalogItems']:
        all_data = dat

        item_uuid = all_data['uuid']
        category_uuids = all_data['sectionUuid']
        Main_category_name = all_category_name_With_UUID.get(category_uuids)
        subCategory_uuid = all_data['subsectionUuid']
        subcategory_name = sub_category.get(subCategory_uuid)
        item_name = all_data['title']
        item_img = all_data['imageUrl']
        item_price = all_data['price']
        raw_price = all_data['priceTagline']['text'].replace("GHS", "")
        # print(f"{item_price} - {raw_price}")
        item_category = all_data['sectionUuid']
        item_sub_category = all_data['sectionUuid']
        count_item += 1

        if item_price == 0:
            json_datamodiyer_data = {
                'itemRequestType': 'ITEM',
                'storeUuid': f'{store_id}',
                'sectionUuid': category_uuids,
                'subsectionUuid': subCategory_uuid,
                'menuItemUuid': item_uuid,
                'diningMode': 'DELIVERY',
                'cbType': 'EATER_ENDORSED',
            }

            response_modifyer = requests.post(
                'https://www.ubereats.com/_p/api/getMenuItemV1',
                headers=headers,
                cookies=cookies,
                json=json_datamodiyer_data,
            )
            sleep(0.3)
            modifyer_data = json.loads(response_modifyer.text)

            try:

                modi_item_name = modifyer_data['data']['title']
                for modi_item in modifyer_data['data']['customizationsList'][0]['options']:
                    modi_option_name = modi_item['title']
                    modi_item_price = modi_item['price']
                    option_uuid = modi_item['uuid']
                    # RAWmodi_item_price = modi_item['priceTagline']['text'].replace("GHS","")
                    # item_option_combo_name = f"{modi_item_name} ** {modi_option_name}"
                    save_in_csv = [Main_category_name, subCategory_uuid, subcategory_name, option_uuid, modi_item_name,
                                   modi_option_name, modi_item_price, item_img]
                    with open(f'{CSV_FILE_NAME}.csv', 'a', newline='') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(save_in_csv)
                        csvFile.close()
                    print(f"{count_item} > {Main_category_name} > {subcategory_name} > {modi_option_name} > {modi_item_price}")
            except:
                pass

        else:
            x = 'x'
            if x == 'x':
                save_in_csv = [Main_category_name, subCategory_uuid, subcategory_name, item_uuid, '', item_name, item_price,
                               item_img]
                with open(f'{CSV_FILE_NAME}.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(save_in_csv)
                    csvFile.close()
                    print(f"{count_item} > {Main_category_name} > {subcategory_name} > {item_name} > {item_price}")

            elif item_name.strip().upper() == "NEW":
                save_in_csv = [Main_category_name, subCategory_uuid, subcategory_name, item_uuid, '', item_name, item_price,
                               item_img]
                with open(f'{CSV_FILE_NAME}.csv', 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(save_in_csv)
                    csvFile.close()
                    print(f"{count_item} > {Main_category_name} > {subcategory_name} > {item_name} > {item_price}")


    if data['data']['pagingInfo']['hasMore'] == True:
        # print(data['data']['pagingInfo']['offset'])
        item_page += 60
    elif data['data']['pagingInfo']['hasMore'] == False:
        stop_data = False
