import requests
import json
import csv
import uuid


with open("C:/Users/quick/PycharmProjects/GUI_App/ADD_InGroceryUberEat.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lin in csv_reader:
        item_uuid = uuid.uuid4()
        # only to create modifyer ids = lin[7]
        Category_ids = lin[2]
        item_name = lin[3]
        product_price = lin[4]
        img_url = lin[5]
        descriptions = ''
        alcholo_yes_no = 0
        print(lin)

        if not img_url == 'None':
            img_url_data = img_url
        else:
            img_url_data = None


        # 0 - NO and 1 = Yes
        AlcoholItem = 0

        if AlcoholItem == 1:
            yes_it_alcoholicitem = True
        elif AlcoholItem == 0:
            yes_it_alcoholicitem = False
        else:
            yes_it_alcoholicitem = False

        # Fort Green Food Market
        store_UUID = '1a5ede99-3c38-5f9a-983f-2dc8c51988bb'
        Item_UUID = item_uuid
        # Category_ids = '899e1ad6-08ef-424f-b1d8-5babd878f3df'
        product_names = item_name.title()

        cookies = {
            # Optional
            'session_id': '{"session_id":"abe01201-18cd-426b-af8b-43a6b369c6b5","session_time_ms":1682541826154}',
            # Importan
            'sid': 'QA.CAESEAoGL4KyBkWAlG2dkBdCVR8Ync_uowYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAMV5kjWlYe7Pocp7xNMadyVJVLAcu_-ejK-3TRlJNKU5AoNP8NbmuLtoQ0v1xRKVGS9L-DjI1XdWPWm1yvwipgToBMUINLnViZXJlYXRzLmNvbQ.nUByM-48QZmnQDYpoh6i1_1Kny8TF4uTiFWQqMMfXsA',
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
            'Referer': f'https://merchants.ubereats.com/manager/menumaker/{store_UUID}/overview?entityType=item&entityUUID={Item_UUID}&categoryUUID={Category_ids}&mode=create',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params2 = {
            'localeCode': 'en-US',
        }

        json_data2 = {
            'storeUUID': f'{store_UUID}',
            'shouldLoadItems': True,
        }

        response2 = requests.post('https://merchants.ubereats.com/manager/menumaker/api/getMenuData', params=params2, cookies=cookies, headers=headers, json=json_data2)
        print(response2)

        data = json.loads(response2.text)
        sections_data = data['data']['menus'][f'{store_UUID}']['sections']
        subsectionsMap_data = data['data']['menus'][f'{store_UUID}']['subsectionsMap']
        params = {
            'localeCode': 'en',
        }

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
                        'createdAt': '2022-09-14T01:05:40.014Z',
                        'updatedAt': '2023-04-13T14:48:13.491Z',
                    },
                },
                {
                    'action': 'update',
                    'menuType': 'MENU_TYPE_FULFILLMENT_PICK_UP',
                    'type': 'menu',
                    'data': {
                        'sections': sections_data,
                        'subsectionsMap': subsectionsMap_data,
                        'displayOptions': {
                            'disableItemInstructions': None,
                            'currencyCode': 'USD',
                            'isMenuV2': True,
                        },
                        'createdAt': '2022-09-14T01:05:40.014Z',
                        'updatedAt': '2023-04-13T14:58:23.362Z',
                    },
                },
                {
                    'action': 'create',
                    'type': 'item',
                    'data': {
                        'customizationUUIDs': {
                            'defaultValue': [],
                        },
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
                                'uberProductType': 'GRAINS_RICE_AND_LEGUMES',
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
                                'defaultValue': f'{descriptions}',
                            },
                            'externalNotes': None,
                            'notes': None,
                            'title': {
                                'defaultValue': f"{product_names}",
                            },
                            'image': {
                                'imageMetadata': {
                                    'imageAspectRatio': 0.6666666666666666,
                                },
                                'imageURL': img_url_data,
                                'rawImageURL': None,
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
                        'attributeExtensions': {
                            'dish_classification': {
                                'foodBusinessOperator': {
                                    'address': None,
                                },
                            },
                            'beverage': {
                                'alcoholByVolume': {},
                                'caffeineAmount': {
                                    'lower': {},
                                    'upper': {},
                                },
                                'coffeeInfo': {},
                            },
                            'medication': {},
                            'nutrition': {
                                'numberOfServingsInterval': {
                                    'lower': {},
                                    'upper': {},
                                },
                                'netQuantity': {
                                    'decimalInterval': {
                                        'lower': {},
                                        'upper': {},
                                    },
                                    'unit': {},
                                },
                                'nutrientsList': [],
                                'servingSize': {
                                    'decimalInterval': {
                                        'lower': {},
                                        'upper': {},
                                    },
                                    'unit': {},
                                },
                                'perServingCalories': None,
                                'perServingKilojoules': None,
                            },
                            'physical_properties': {},
                            'price': {
                                'containerDeposit': {
                                    'amountE5': {},
                                },
                            },
                            'product': {},
                        },
                        'paymentInfo': {
                            'priceInfo': {
                                'defaultValue': {
                                    'price': {
                                        'low': int(product_price),
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
                {
                    'action': 'update',
                    'type': 'item',
                    'data': {
                        'customizationUUIDs': {
                            'defaultValue': [],
                        },
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
                                'uberProductType': 'GRAINS_RICE_AND_LEGUMES',
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
                                'defaultValue': f"{descriptions}",
                            },
                            'externalNotes': None,
                            'notes': None,
                            'title': {
                                'defaultValue': f"{product_names}",
                            },
                            'image': {
                                'imageMetadata': {
                                    'imageAspectRatio': 0.6666666666666666,
                                },
                                'imageURL': img_url_data,
                                'rawImageURL': None,
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
                        'attributeExtensions': {
                            'dish_classification': {
                                'foodBusinessOperator': {
                                    'address': None,
                                },
                            },
                            'beverage': {
                                'alcoholByVolume': {},
                                'caffeineAmount': {
                                    'lower': {},
                                    'upper': {},
                                },
                                'coffeeInfo': {},
                            },
                            'medication': {},
                            'nutrition': {
                                'numberOfServingsInterval': {
                                    'lower': {},
                                    'upper': {},
                                },
                                'netQuantity': {
                                    'decimalInterval': {
                                        'lower': {},
                                        'upper': {},
                                    },
                                    'unit': {},
                                },
                                'nutrientsList': [],
                                'servingSize': {
                                    'decimalInterval': {
                                        'lower': {},
                                        'upper': {},
                                    },
                                    'unit': {},
                                },
                                'perServingCalories': None,
                                'perServingKilojoules': None,
                            },
                            'physical_properties': {},
                            'price': {
                                'containerDeposit': {
                                    'amountE5': {},
                                },
                            },
                            'product': {},
                        },
                        'paymentInfo': {
                            'priceInfo': {
                                'defaultValue': {
                                    'price': {
                                        'low': int(product_price),
                                        'high': 0,
                                        'unsigned': False,
                                    },
                                },
                                'overrides': None,
                            },
                            'pricingPolicy': None,
                        },
                    },
                    'validate': None,
                    'menuType': 'MENU_TYPE_FULFILLMENT_PICK_UP',
                    'parentObjectUUIDs': [
                        f'{Category_ids}',
                    ],
                },
            ],
            'shouldLoadItems': True,
            'cityId': 5,
            'internalTags': [
                {
                    'uuid': 'ca4f2434-1a17-4691-b2cd-360cd0f4914d',
                    'name': 'createdbysfdc',
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
                    'uuid': '96e8d56c-7384-4769-9ecb-b48f32e00e62',
                    'name': 'enable_restaurant_alcohol_sales_hours',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '881330fb-d839-4972-b000-54e48eab080a',
                    'name': 'usc_ob_nv_reconciled',
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
                    'uuid': '3f748007-ed6b-4038-999b-da430c87db94',
                    'name': 'alcohol_warning_sent_1',
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
                    'uuid': '3e606252-d37d-4c40-ac43-ab67d9cc5e4c',
                    'name': 'houseads_q12023_xp',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '4f65488d-b743-46b7-96f4-fd431f6601ee',
                    'name': 'use_sections_as_categories',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
            ],
            'countryCode': 'US',
            'storeUUID': f'{store_UUID}',
        }

        response = requests.post(
            'https://merchants.ubereats.com/manager/menumaker/api/upsertMenus',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data

        )
        print(response.status_code)
        print(item_name)
