import json

import requests
import csv
import uuid

store_UUID = '1a5ede99-3c38-5f9a-983f-2dc8c51988bb'

cookies = {
    # Optional
    'session_id': '{"session_id":"3b824cbc-5218-4000-a562-44e8633a2932","session_time_ms":1652052276972}',
    # Important
    'sid': 'QA.CAESEOnsiLgGeEKUraJFaVP0gXMY2J_woQYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAjRR6rL8q2QHxJ8qVxrYHldvt1AyptoVNyqSrywdKkhEbrD1DhctH3rXc0ZpdegOCLcVIcYMppBskTk2816qKNzoBMUINLnViZXJlYXRzLmNvbQ.MOlYc8x0Qh1AuigtX8cdbRpjkbtU0rLEBOg7UbcW6QA',
    'selectedRestaurant': f'{store_UUID}',
}

headers = {
    'Host': 'merchants.ubereats.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'X-Csrf-Token': 'x',
    'Origin': 'https://merchants.ubereats.com',
    'Referer': f'https://merchants.ubereats.com/manager/menumaker/{store_UUID}/items',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'localeCode': 'en',
}

json_data = {
    'storeUUID': '1a5ede99-3c38-5f9a-983f-2dc8c51988bb',
    'shouldLoadItems': True,
}

response = requests.post(
    'https://merchants.ubereats.com/manager/menumaker/api/getMenuData',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,

)
print(response.status_code)
Row_data = json.loads(response.text)

data = Row_data['data']['menus'][store_UUID]['entities']['itemsMap']
for all_data in data:
    try:
        check_UPC = int(data[all_data]['vendorInfo']['externalID'])
        upc_code = check_UPC
        item_name = data[all_data]['itemInfo']['title']['defaultValue']
        item_price = data[all_data]['paymentInfo']['priceInfo']['defaultValue']['price']['low']
        # print(data[all_data]['vendorInfo']['externalID'])

        row = [item_name,upc_code,item_price]
        with open(
                f'Uber_invetory.csv',
                'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()

    except:
        pass
