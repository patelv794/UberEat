import requests
import json
import csv
import uuid



# Get Modifiyer ID
def Get_Modifiyer_IDS(modifiyer_name):
    Modifiyer = data['data']['menus'][f'{store_UUID}']['entities']['customizationsMap']
    for modi in Modifiyer:
        Modi_name = Modifiyer[modi]['title']['defaultValue']
        Modi_UUID = Modifiyer[modi]['uuid']
        if modifiyer_name.strip().upper() == Modi_name.strip().upper():
            return Modi_UUID


with open("C:/Users/Admin/PycharmProjects/Beer Inventory - 2022/Only_brand.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lin in csv_reader:
        item_uuid = uuid.uuid4()
        # only to create modifyer ids = lin[7]
        category_uuid = lin[3]
        item_name = lin[2]
        img_url = lin[4]
        item_prices_modifiyer11 = lin[2].strip()
        alcholo_yes_no = 1
        print(lin)

        if not img_url == 'None':
            img_url_data = img_url
        else:
            img_url_data = None


        # Quick Smoke
        store_UUID = '1a5ede99-3c38-5f9a-983f-2dc8c51988bb'
        Item_UUID = item_uuid
        Category_ids = category_uuid
        product_names = item_name.title()

        # 0 - NO and 1 = Yes
        AlcoholItem = alcholo_yes_no

        if AlcoholItem == 1:
            yes_it_alcoholicitem = True
        elif AlcoholItem == 0:
            yes_it_alcoholicitem = False
        else:
            yes_it_alcoholicitem = False

        cookies1 = {
            # Optional
            'session_id': '{"session_id":"3b824cbc-5218-4000-a562-44e8633a2932","session_time_ms":1652052276972}',
            # Important
            'sid': 'QA.CAESENUnWjCmlUeqmYp43a-hu24Yj6G0mwYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAvqduMBDTLuW-L7vFFRZeUzatm7xu30x8N-ULMO1PkQJrzTEZ2B0HWPCtVbkIGXTe2FxRW18JHmSLOsozBfkHjDoBMUINLnViZXJlYXRzLmNvbQ.htda4Qt3Is1X9hxI8QK4a9dUONyzWNFz0Qt3jOXSASU',
            'selectedRestaurant': f'{store_UUID}',
        }

        headers1 = {
            'authority': 'merchants.ubereats.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://merchants.ubereats.com',
            'referer': f'https://merchants.ubereats.com/manager/menumaker/{store_UUID}/overview?entityType=item&entityUUID={Item_UUID}&categoryUUID={Category_ids}&mode=create',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'x-csrf-token': 'x',
        }

        params1 = {
            'localeCode': 'en-US',
        }

        json_data1 = {}

        response1 = requests.post('https://merchants.ubereats.com/manager/menumaker/api/listProductTypes', params=params1, cookies=cookies1, headers=headers1, json=json_data1)
        print(response1)

        # ---------------------

        params2 = {
            'localeCode': 'en-US',
        }

        json_data2 = {
            'storeUUID': f'{store_UUID}',
            'shouldLoadItems': True,
        }

        response2 = requests.post('https://merchants.ubereats.com/manager/menumaker/api/getMenuData', params=params2, cookies=cookies1, headers=headers1, json=json_data2)
        print(response2)

        # with open('CSV/Quick Smoke Shop Inventry/json_data.txt', 'w') as f:
        #     f.write(f'{response2.text}')


        json_data3 = {
            'entityUUID': f'{Item_UUID}',
            'storeUUID': f'{store_UUID}',
        }

        response3 = requests.post('https://merchants.ubereats.com/manager/menumaker/api/searchParents', params=params2, cookies=cookies1, headers=headers1, json=json_data3)
        print(response3)

        data = json.loads(response2.text)

        try:
            item_prices_modifiyer = item_prices_modifiyer11.replace('.', '')
            item_prices_modifiyer = int(item_prices_modifiyer)
            modifiyer_name_def = ''
            if_yes_modifyer = {'defaultValue': []}

        except:
            modifiyer_name_def = Get_Modifiyer_IDS(item_prices_modifiyer11)
            if_yes_modifyer = {'defaultValue': [
                f'{modifiyer_name_def}'
            ],}
            item_prices_modifiyer = 0

        product_price = item_prices_modifiyer
        sections_data = data['data']['menus'][f'{store_UUID}']['sections']
        subsectionsMap_11 = data['data']['menus'][f'{store_UUID}']['subsectionsMap'][f'{Category_ids}']
        subsectionsMap_data = data['data']['menus'][f'{store_UUID}']['subsectionsMap']
        created_at = data['data']['menus'][f'{store_UUID}']['createdAt']
        updated_at = data['data']['menus'][f'{store_UUID}']['updatedAt']

        # with open('find modifiyers.txt', 'w') as f:
        #     f.write(f'{data}')
        # 27fb9404-8282-4512-b20e-aaf127194737
        new_data = subsectionsMap_11['displayItems']

        student = {
        'type': 'item',
        'uuid': f'{Item_UUID}',
        }

        # append this dictionary to the empty list
        new_data.append(student)



        json_data = {
            'changes': [
                {
                    'action': 'update',
                    'menuType': 'MENU_TYPE_FULFILLMENT_DELIVERY',
                    'type': 'menu',
                    'data': {
                        'sections': sections_data,
                        'subsectionsMap': subsectionsMap_data,
                        'displayOptions': {
                            'disableItemInstructions': None,
                            'currencyCode': 'USD',
                            'isMenuV2': True,
                        },
                        'createdAt': f'{created_at}',
                        'updatedAt': f'{updated_at}',
                    },
                },
                {
                    'action': 'create',
                    'type': 'item',
                    'data': {
                        'customizationUUIDs':
                            if_yes_modifyer,
                        'dishInfo': {
                            'classifications': {
                                'alcoholicItems': AlcoholItem,
                                'hasAlcoholicItems': yes_it_alcoholicitem,
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
                                'defaultValue': f'{product_names}',
                            },
                            'image': {
                                'imageURL':img_url_data,
                                'rawImageURL': None,
                                'imageMetadata': {
                                    'imageAspectRatio': 0.6666666666666666,
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
                        'uuid': f'{Item_UUID}',
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
                                        'low': product_price,
                                        'high': 0,
                                        'unsigned': False,
                                    },
                                },
                                'overrides': None,
                            },
                            'pricingPolicy': None,
                        },
                    },
                    'menuType': 'MENU_TYPE_FULFILLMENT_DELIVERY',
                    'parentObjectUUIDs': [
                        f'{Category_ids}',
                    ],
                },
            ],
            'shouldLoadItems': True,
            'cityId': 5,
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
            ],
            'countryCode': 'US',
            'storeUUID': f'{store_UUID}',
        }

        response = requests.post('https://merchants.ubereats.com/manager/menumaker/api/upsertMenus', params=params2, cookies=cookies1, headers=headers1, json=json_data)
        print(response)



        # if not response.status_code == 200:
        #     user_yes = input(f'{item_name}: Error ADDING... ')
        #     if user_yes == 'ok':
        #         pass

