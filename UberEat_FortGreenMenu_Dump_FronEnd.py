
import csv
import json
from time import sleep
import requests
import pandas as pd




store_id = "1a5ede99-3c38-5f9a-983f-2dc8c51988bb"
csv_file_name = 'CSV/Just_beer-08-24-23.csv'

def Update_price_img(item_number,update_price,update_imgurl):
    # reading the csv file
    df = pd.read_csv(csv_file_name, encoding='latin1')
    # updating the column value/data
    df.loc[item_number++1, 'Price'] = f"{update_price}"
    df.loc[item_number++1, 'Image URL'] = f"{update_imgurl}"
    # writing into the file
    df.to_csv(csv_file_name, index=False, encoding='latin1')
    print(f"Price Updated: {item_number} - ${update_price}")

# try:
#     availabel_items_inCSV = []
#     with open(csv_file_name, "r") as csv_file_login_data:
#         csv_reader_data = csv.reader(csv_file_login_data, delimiter=',')
#         for lin_data in csv_reader_data:
#             # print(lin_data)
#             to_append = f"{lin_data[0]} > {lin_data[1]} > {lin_data[2]} > {lin_data[3]} > {lin_data[4]}"
#             availabel_items_inCSV.append(to_append.upper())
# except:
#     availabel_items_inCSV = []
#     pass


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
    json=json_data_category,
)


sleep(1)
data = json.loads(response_category.text)
raw_data = data['data']['catalogSectionsMap'][store_id]

for all_raw_data in raw_data:
    catalogSectionUUID = all_raw_data['catalogSectionUUID']
    category_name = all_raw_data['payload']['standardItemsPayload']['title']['text']
    print(category_name)
    all_category_name_With_UUID[catalogSectionUUID] = category_name


for category in all_category_name_With_UUID:

    category_uuuid = category
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
            },
            'pagingInfo': {
                'enabled': True,
                'offset': item_page,
            },
        }

        response = requests.post(
            'https://www.ubereats.com/_p/api/getCatalogPresentationV1',
            headers=headers,
            json=json_data,
        )
        print(response.status_code)
        data = json.loads(response.text)
        sleep(2)

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
            item_category = all_data['sectionUuid']
            item_sub_category = all_data['sectionUuid']
            count_item +=1
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
                    json=json_datamodiyer_data,
                )
                sleep(2)
                try:
                    modifyer_data = json.loads(response_modifyer.text)
                except:
                    try:
                        modifyer_data = json.loads(response_modifyer.text)
                    except:
                        modifyer_data = json.loads(response_modifyer.text)

                try:
                    modi_item_name = modifyer_data['data']['title']
                    for modi_item in modifyer_data['data']['customizationsList'][0]['options']:
                        modi_option_name = modi_item['title']
                        modi_item_price = modi_item['price']
                        # item_option_combo_name = f"{modi_item_name} ** {modi_option_name}"
                        # check_first = f"{Main_category_name} > {subcategory_name} > {item_option_combo_name} > {modi_item_price} > {item_img}"
                        # if not check_first.upper() in availabel_items_inCSV:
                        #     print(f"{count_item} > {Main_category_name} > {subcategory_name} > {item_name} > {item_price}")
                        save_in_csv1 = [Main_category_name, subcategory_name, modi_item_name, modi_option_name, modi_item_price, item_img]
                        with open(csv_file_name, 'a', newline='') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(save_in_csv1)
                            csvFile.close()
                        print(save_in_csv1)
                except:
                    pass
            else:
                # try:
                    # check_second = f"{Main_category_name} > {subcategory_name} > {item_name} > {item_price} > {item_img}"
                    # if not check_second.upper() in availabel_items_inCSV:
                    #     print(f"{count_item} > {Main_category_name} > {subcategory_name} > {item_name} > {item_price}")
                save_in_csv2 = [Main_category_name, subcategory_name, item_name,'', item_price, item_img]
                with open(csv_file_name, 'a', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(save_in_csv2)
                    csvFile.close()
                print(save_in_csv2)
                # except:
                #     save_in_csv3 = [Main_category_name, subcategory_name, item_name,'', item_price, item_img,'FIX']
                #     with open(csv_file_name, 'a',encoding='utf-8', newline='') as csvFile:
                #         writer = csv.writer(csvFile)
                #         writer.writerow(save_in_csv3)
                #         csvFile.close()

        if data['data']['pagingInfo']['hasMore'] == True:
            # print(data['data']['pagingInfo']['offset'])
            item_page += 60
        elif data['data']['pagingInfo']['hasMore'] == False:
            stop_data = False



# for i in data['data']['catalog']:
#     print(i)
