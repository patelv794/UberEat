import json

import requests
import csv
import uuid

# Error adding Price on sub item getting $0
with open("C:/Users/Admin/PycharmProjects/Beer Inventory - 2022/Only_brand.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lin in csv_reader:
        item_uuid = uuid.uuid4()
        item_name_brand = lin[2].strip()
        print(item_name_brand)

        selected_data = []
        with open("C:/Users/Admin/PycharmProjects/Beer Inventory - 2022/DRIZLY_BEER_DATA_Fort_Green.csv","r") as csv_file2:
            csv_reader2 = csv.reader(csv_file2, delimiter=',')
            for lin2 in csv_reader2:
                sub_item_UUID_1 = uuid.uuid4()
                sub_item_UUID_2 = uuid.uuid4()
                items_names = lin2[1]
                sub_item = lin2[2].strip()
                sub_price11 = lin2[3].strip()
                sub_price = sub_price11.replace('.','')
                if items_names.strip().upper() == item_name_brand.strip().upper():
                    selected_data.append(f"{sub_item_UUID_1}<>{sub_item_UUID_2}<>{sub_item}<>{sub_price}")

        modifiyer_Item_UUID = item_uuid
        store_UUID = '1a5ede99-3c38-5f9a-983f-2dc8c51988bb'
        modifiyer_product_names = item_name_brand.title()


        cookies = {
            # Optional
            'session_id': '{"session_id":"3b824cbc-5218-4000-a562-44e8633a2932","session_time_ms":1652052276972}',
            # Important
            'sid': 'QA.CAESENUnWjCmlUeqmYp43a-hu24Yj6G0mwYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAvqduMBDTLuW-L7vFFRZeUzatm7xu30x8N-ULMO1PkQJrzTEZ2B0HWPCtVbkIGXTe2FxRW18JHmSLOsozBfkHjDoBMUINLnViZXJlYXRzLmNvbQ.htda4Qt3Is1X9hxI8QK4a9dUONyzWNFz0Qt3jOXSASU',
            'selectedRestaurant': f'{store_UUID}',
        }

        headers = {
            'authority': 'merchants.ubereats.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://merchants.ubereats.com',
            'referer': f'https://merchants.ubereats.com/manager/menumaker/{store_UUID}/overview?entityType=modifier_group&entityUUID={modifiyer_Item_UUID}&mode=create',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'x-csrf-token': 'x',
        }

        params = {
            'localeCode': 'en-US',
        }

        Final_whole_json_data = []
        option_uuis = []

        for select_data in selected_data:
            data_selected = select_data.split('<>')
            sub_uuid_11 = data_selected[0]
            sub_uuid_22 = data_selected[1]
            sub_product = data_selected[2]
            sub_product_price = int(data_selected[3])

            multiple_sub_item_json = {

            'action': 'create',
            'type': 'item',
            'data': {
                'customizationUUIDs': {
                    'defaultValue': [],
                },
                'dishInfo': {
                    'classifications': {
                        'alcoholicItems': 0,
                        'hasAlcoholicItems': False,
                        'cuisineUUID': None,
                        'dietaryInfo': None,
                        'isEntree': None,
                        'isHot': None,
                        'mealTypeUUID': None,
                        'proteinTypeUUID': None,
                        'dietaryLabels': None,
                        'uberProductType': None,
                        'uberProductTraits': [],
                    },
                    'nutritionalInfo': {
                        'caloricInfo': None,
                        'jouleInfo': None,
                    },
                },
                'itemInfo': {
                    'badges': None,
                    'description': {
                        'defaultValue': None,
                    },
                    'externalNotes': None,
                    'notes': None,
                    'title': {
                        'defaultValue': f'{sub_product}',
                    },
                    'image': {
                        'imageURL': None,
                        'rawImageURL': None,
                        'imageMetadata': {
                            'imageAspectRatio': None,
                        },
                    },
                },
                'suspensionInfo': {
                    'defaultValue': {
                        'suspendUntil': '',
                        'suspendReason': '',
                        'suspendUntilMilliseconds': None,
                    },
                },
                'taxLabelInfo': {
                    'defaultValue': None,
                },
                'taxInfo': {
                    'taxRate': None,
                    'vatRate': None,
                },
                # 84c24766-26c2-4c98-bf86-72793f6b0626
                'uuid': f'{sub_uuid_11}',
                'vendorInfo': {
                    'externalData': None,
                    'externalID': None,
                },
                'productInfo': {
                    'externalProductIDType': None,
                    'externalProductIDValue': None,
                    'targetMarket': None,
                },
                'paymentInfo': {
                    'priceInfo': {
                        'defaultValue': {
                            'price': {
                                'low': sub_product_price,
                                'high': 0,
                                'unsigned': False,
                            },
                        },
                        'overrides': [
                            {
                                'contextType': 'CUSTOMIZATION_UUID',
                                'contextValue': f'{sub_uuid_22}',
                                'overriddenValue': {
                                    'price': {
                                        'low': sub_product_price,
                                        'high': 0,
                                        'unsigned': False,
                                    },
                                },
                            },
                        ],
                    },
                    'pricingPolicy': None,
                },
                'quantityInfo': {
                    'overrides': [
                        {
                            'contextType': 'CUSTOMIZATION_UUID',
                            'contextValue': f'{sub_uuid_22}',
                            'overriddenValue': {
                                'defaultQuantity': None,
                                'maxPermitted': 1,
                            },
                        },
                    ],
                },
            },
            'menuType': 'MENU_TYPE_FULFILLMENT_DELIVERY',
        }
            Final_whole_json_data.append(multiple_sub_item_json)

            option_data = {'uuid' : sub_uuid_11}
            option_uuis.append(option_data)



        append_jason_part_2 = {

                    'action': 'create',
                    'type': 'modifier_group',
                    'data': {
                        'title': {
                            'defaultValue': f'{modifiyer_product_names}',
                        },
                        'options': option_uuis,
                        'quantityInfo': {
                            'defaultValue': {
                                'maxPermitted': int(len(option_uuis)),
                                'minPermitted': 1,
                            },
                        },
                        'vendorInfo': {
                            'groupUUID': None,
                            'externalID': None,
                            'externalData': '',
                        },
                        'externalNotes': '',
                        'uuid': f'{item_uuid}',
                    },
                    'menuType': 'MENU_TYPE_FULFILLMENT_DELIVERY',
                }
        Final_whole_json_data.append(append_jason_part_2)

        json_data = {
            'changes': Final_whole_json_data,
            'shouldLoadItems': True,
            'cityId': 1541,
            'internalTags': [
                {
                    'uuid': 'dcd78a6f-5cfb-435e-9836-49d4b605f7cb',
                    'name': 'EATS_SELF_SIGN_UP',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '2aac4591-ff7f-4940-a9ea-2bdde16e0e1d',
                    'name': 'post_pickle',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'f9fc75df-eb59-4847-8766-64edf10d3892',
                    'name': 'menu_maker_enabled',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'c88fe4ff-4dd2-470e-8e05-237993e525d0',
                    'name': 'nyft21_tag1',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '3f4bbfcc-51c7-4966-ae13-0d26aa445ff5',
                    'name': 'has_restaurant_promotions',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '8b3e1f4b-95b5-47ea-83b3-198eb1253c38',
                    'name': 'tob_removal_1',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '449c45b7-d0c4-4193-a210-96b7043674e4',
                    'name': 'tob_removal_2',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '3f748007-ed6b-4038-999b-da430c87db94',
                    'name': 'alcohol_warning_sent_1',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '9833db5f-f81e-4ef5-b422-714d8ef8c1e4',
                    'name': 'tob_removal_3',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'b24c5293-da5b-4ff9-b47d-6f5c607d26e2',
                    'name': 'alcohol_warning_sent_2',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '406423fe-897a-49bc-a62d-70b566572b14',
                    'name': 'alcohol_warning_sent_3',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'e1a395ae-f4bc-45dd-b325-8895ea1c5a38',
                    'name': 'tob_removal_4',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'd8ac5d97-1bc9-43ff-89b4-a9c9db1f9607',
                    'name': 'alcohol interested',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '1ff5eeac-0064-4a3e-a3ce-89a05de1a30f',
                    'name': 'trigger_index',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '96e8d56c-7384-4769-9ecb-b48f32e00e62',
                    'name': 'enable_restaurant_alcohol_sales_hours',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'dfd9ccef-abce-4d18-a60c-8bd4f6efdd8c',
                    'name': 'alcohol_sku_verified',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '60f9aff5-4c71-44b9-831d-27fc5b7764c4',
                    'name': 'alcohol_warning_sent_4',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '6024e872-6fa9-4c34-8c25-2582a93b5544',
                    'name': 'top_eats',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': 'cb286ce3-9681-4e7d-8238-d75e1cca7e9d',
                    'name': 'alcohol_warning_sent_5',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
            ],
            'countryCode': 'US',
            'storeUUID': f'{store_UUID}',
        }

        response = requests.post('https://merchants.ubereats.com/manager/menumaker/api/upsertMenus', params=params, cookies=cookies, headers=headers, json=json_data)
        print(response.status_code)
        success = json.loads(response.text)
        print(f'--------------------------------------{success["status"]}')





