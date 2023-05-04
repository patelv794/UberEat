
import csv
import json

import requests


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
    'storeUuid': '979fe32b-6db1-5ac3-b3b8-49af46ddef57',
    'sfNuggetCount': 50,
    'cbType': 'EATER_ENDORSED',
}
response_category = requests.post(
    'https://www.ubereats.com/_p/api/getStoreV1',
    headers=headers,
    json=json_data_category,
)

data = json.loads(response_category.text)
raw_data = data['data']['catalogSectionsMap']['979fe32b-6db1-5ac3-b3b8-49af46ddef57']

for all_raw_data in raw_data:
    catalogSectionUUID = all_raw_data['catalogSectionUUID']
    category_name = all_raw_data['payload']['standardItemsPayload']['title']['text']
    print(category_name)
    all_category_name_With_UUID[catalogSectionUUID] = category_name



stop_data = True
item_page = 0
count_item = 0
sub_category = {}
while stop_data:

    category_id = ["a660c916-2ecd-475d-9d81-945a2bfdadc8"]
    json_data = {
        'storeFilters': {
            'storeUuid': '979fe32b-6db1-5ac3-b3b8-49af46ddef57',
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

    if not sub_category:
        for get_subCat in data['data']['catalog']:
            uuid = get_subCat['catalogSectionUUID']
            name = get_subCat['payload']['standardItemsPayload']['title']['text']
            sub_category[uuid] = name
            # sub_category['cat_uuid'] = uuid

    for dat in data['data']['catalog'][0]['payload']['standardItemsPayload']['catalogItems']:
        all_data = dat
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
        print(f"{count_item} > {Main_category_name} > {subcategory_name} > {item_name} > {item_price}")

    if data['data']['pagingInfo']['hasMore'] == True:
        # print(data['data']['pagingInfo']['offset'])
        item_page += 60
    elif data['data']['pagingInfo']['hasMore'] == False:
        stop_data = False

#
#         save_in_csv = [category_name,items_name,item_price,item_description,item_img]
#         print(items_name)
#         # with open(f'Fort Green Irish & British11111.csv', 'a', newline='') as csvFile:
#         #     writer = csv.writer(csvFile)
#         #     writer.writerow(save_in_csv)
#         #     csvFile.close()

# for i in data['data']['catalog']:
#     print(i)

