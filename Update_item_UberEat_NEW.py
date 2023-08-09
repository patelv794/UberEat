
import http.client
import csv
import json


conn = http.client.HTTPSConnection("merchants.ubereats.com")

with open("Chips.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lin in csv_reader:
        print(lin)
        category_uuid = lin[1]
        item_uuid = lin[3]
        item_name = lin[5]
        item_price = int(lin[6].strip().replace('.',''))
        image_urllink = lin[7]
        json_data = {
            'changes': [
                {
                    'action': 'update',
                    'type': 'item',
                    'data': {
                        'uuid': f"{item_uuid}",
                        'itemInfo': {
                            'title': {
                                'defaultValue': f"{item_name}",
                                'overrides': None,
                            },
                            # 'description': {
                            #     'defaultValue': '',
                            #     'overrides': None,
                            # },
                            "image": {
                                "imageURL": f"{image_urllink}",
                                "rawImageURL": None,
                                "imageMetadata": {
                                    "imageAspectRatio": 0.66666666,
                                },
                            },
                        },
                        'paymentInfo': {
                            'priceInfo': {
                                'defaultValue': {
                                    'price': {
                                        'low': item_price,
                                        'high': 0,
                                        'unsigned': False,
                                    },
                                },
                            },
                        },
                        'createdAt': '2023-06-07T12:50:49.685Z',
                        'updatedAt': '2023-07-24T07:29:11.403Z',
                    },
                    'menuType': 'MENU_TYPE_FULFILLMENT_DELIVERY',
                    'parentObjectUUIDs': [],
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
                {
                    'uuid': 'af538241-d266-44ad-9abf-7f7325cdbb1e',
                    'name': 'usc_visibility_tier_2',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '37fe3f48-e912-4724-a741-9bb87f6fb0e5',
                    'name': 'usc_quality_full_access',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
                {
                    'uuid': '3f4bbfcc-51c7-4966-ae13-0d26aa445ff5',
                    'name': 'has_restaurant_promotions',
                    'type': 'INTERNAL_TAG',
                    'localizedName': None,
                },
            ],
            'countryCode': 'US',
            'storeUUID': '1a5ede99-3c38-5f9a-983f-2dc8c51988bb',
        }
        payload = str(json.dumps(json_data))

        headers = {

            'cookie': "sid=QA.CAESEAMp4aohmEYHsdwQTsUEvsYYysvapwYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAuls0NXag8KIFUJF1KraVEIIYMPE22hjPzMqmaBHhUmonK9m52szMVeBU1WKVKag-TrvxL7YAMTgg9RkmZREjvjoBMUINLnViZXJlYXRzLmNvbQ.KVTtKa5MHi1KLy5XEAGOH-eXo2Hc1ELVQ_T9Mkp2E-8;",
            'Host': "merchants.ubereats.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
            'Accept': "*/*",
            'Accept-Language': "en-US,en;q=0.5",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/json",
            'X-Csrf-Token': "x",
            # 'Content-Length': "4157",
            'Origin': "https://merchants.ubereats.com",
            'Referer': f"https://merchants.ubereats.com/manager/menumaker/1a5ede99-3c38-5f9a-983f-2dc8c51988bb/overview?entityType=item&entityUUID={item_uuid}&mode=edit",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Te': "trailers"
            }

        conn.request("POST", "/manager/menumaker/api/upsertMenus?localeCode=en", payload, headers)

        res = conn.getresponse()
        data = res.read()
        print(item_name)





# Second Version

# import http.client
# import csv
# import json
#
#
#
# conn = http.client.HTTPSConnection("merchants.ubereats.com")
#
#
# with open("Talanti Ice Cream.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lin in csv_reader:
#         print(lin)
#         category_uuid = lin[2]
#         item_uuid = lin[4]
#         item_name = lin[5]
#         item_price = int(lin[6].strip().replace('.',''))
#         image_urllink = lin[7]
#
#         # payload = '{"changes":[f{"action":"update","type":"item","data":{"uuid":"48c9c273-f746-41d8-8f4f-8525e66961c8","itemInfo":{"title":{"defaultValue":"HÃ¤agen-Dazs Ice Cream - ANY 3 Pints","overrides":null},"description":{"defaultValue":"","overrides":null},"image":{"imageURL":null,"rawImageURL":null,"imageMetadata":{"imageAspectRatio":null}},"badges":null,"notes":null,"externalNotes":null,"additionalImages":null,"brandName":null,"locationInformation":null,"functionalName":null},"paymentInfo":{"priceInfo":{"defaultValue":{"price":{"low":2799,"high":0,"unsigned":false}},"overrides":null},"pricingPolicy":null},"dishInfo":{"nutritionalInfo":{"allergens":null,"caloricInfo":null,"jouleInfo":null},"classifications":{"cuisineUUID":null,"mealTypeUUID":null,"proteinTypeUUID":null,"hasSide":null,"isHot":null,"isEntree":null,"alcoholicItems":0,"hasAlcoholicItems":false,"preparationType":null,"drinkInfo":null,"serviceType":null,"foodInfo":null,"classificationLabels":null,"dietaryInfo":null,"dietaryLabels":null,"restrictedItem":null,"gpcCode":null,"packageKey":null,"uberProductType":"ICE_CREAM_AND_NOVELTIES","uberProductTraits":[],"ingredients":null,"additives":null,"uberProductTypeV2":{"value":"ICE_CREAM_AND_NOVELTIES","productTypeMetadata":{"provider":"PRODUCT_TYPE_PROVIDER_MERCHANT","confidence":null}}}},"customizationUUIDs":{"defaultValue":null,"overrides":null},"suspensionInfo":{"defaultValue":{"suspendUntil":"","suspendReason":"","suspendUntilMilliseconds":null},"overrides":null},"vendorInfo":{"externalID":"HÃ¤agen-Dazs_Ice_Crea_99800","externalData":null,"groupUUID":null,"customizationTemplateUUID":null},"tags":null,"quantityInfo":null,"taxLabelInfo":{"defaultValue":null},"createdAt":"2023-08-05T23:15:36.903Z","updatedAt":"2023-08-05T23:15:36.903Z","visibility":null,"productInfo":{"externalProductIDType":null,"externalProductIDValue":null,"targetMarket":null},"bundledItems":null,"attributeExtensions":{"dish_classification":{"foodBusinessOperator":{"address":null}},"beverage":{"alcoholByVolume":{},"caffeineAmount":{"lower":{},"upper":{}},"coffeeInfo":{}},"medication":{},"nutrition":{"numberOfServingsInterval":{"lower":{},"upper":{}},"netQuantity":{"decimalInterval":{"lower":{},"upper":{}},"unit":{}},"nutrientsList":[],"servingSize":{"decimalInterval":{"lower":{},"upper":{}},"unit":{}},"perServingCalories":null,"perServingKilojoules":null},"physical_properties":{},"price":{"containerDeposit":{"amountE5":{}}},"product":{}},"sellingInfo":null,"metadata":null,"productUUID":null,"catalogIdentifiers":null,"taxInfo":{"taxRate":null,"vatRate":null}},"validate":{"entityType":"item","entityUUID":"48c9c273-f746-41d8-8f4f-8525e66961c8"},"menuType":"MENU_TYPE_FULFILLMENT_DELIVERY","parentObjectUUIDs":["4b15b463-c137-4158-95fb-29ebed6fce54"]}],"shouldLoadItems":true,"cityId":5,"internalTags":[{"uuid":"ca4f2434-1a17-4691-b2cd-360cd0f4914d","name":"createdbysfdc","type":"INTERNAL_TAG","localizedName":null},{"uuid":"2aac4591-ff7f-4940-a9ea-2bdde16e0e1d","name":"post_pickle","type":"INTERNAL_TAG","localizedName":null},{"uuid":"f9fc75df-eb59-4847-8766-64edf10d3892","name":"menu_maker_enabled","type":"INTERNAL_TAG","localizedName":null},{"uuid":"96e8d56c-7384-4769-9ecb-b48f32e00e62","name":"enable_restaurant_alcohol_sales_hours","type":"INTERNAL_TAG","localizedName":null},{"uuid":"881330fb-d839-4972-b000-54e48eab080a","name":"usc_ob_nv_reconciled","type":"INTERNAL_TAG","localizedName":null},{"uuid":"dfd9ccef-abce-4d18-a60c-8bd4f6efdd8c","name":"alcohol_sku_verified","type":"INTERNAL_TAG","localizedName":null},{"uuid":"3f748007-ed6b-4038-999b-da430c87db94","name":"alcohol_warning_sent_1","type":"INTERNAL_TAG","localizedName":null},{"uuid":"3e606252-d37d-4c40-ac43-ab67d9cc5e4c","name":"houseads_q12023_xp","type":"INTERNAL_TAG","localizedName":null},{"uuid":"4f65488d-b743-46b7-96f4-fd431f6601ee","name":"use_sections_as_categories","type":"INTERNAL_TAG","localizedName":null},{"uuid":"af538241-d266-44ad-9abf-7f7325cdbb1e","name":"usc_visibility_tier_2","type":"INTERNAL_TAG","localizedName":null},{"uuid":"3f4bbfcc-51c7-4966-ae13-0d26aa445ff5","name":"has_restaurant_promotions","type":"INTERNAL_TAG","localizedName":null},{"uuid":"37fe3f48-e912-4724-a741-9bb87f6fb0e5","name":"usc_quality_full_access","type":"INTERNAL_TAG","localizedName":null}],"countryCode":"US","storeUUID":"1a5ede99-3c38-5f9a-983f-2dc8c51988bb"}'.encode()
#         json_data = {
#             "changes": [
#                 {
#                     "action": "update",
#                     "type": "item",
#                     "data": {
#                         "uuid": f"{item_uuid}",
#                         "itemInfo": {
#                             "title": {
#                                 "defaultValue": f"{item_name}",
#                                 "overrides": None,
#                             },
#                             "description": {
#                                 "defaultValue": "",
#                                 "overrides": None,
#                             },
#                             "image": {
#                                 "imageURL": f"{image_urllink}",
#                                 "rawImageURL": None,
#                                 "imageMetadata": {
#                                     "imageAspectRatio": 1,
#                                 },
#                             },
#                             "badges": None,
#                             "notes": None,
#                             "externalNotes": None,
#                             "additionalImages": None,
#                             "brandName": None,
#                             "locationInformation": None,
#                             "functionalName": None,
#                         },
#                         "paymentInfo": {
#                             "priceInfo": {
#                                 "defaultValue": {
#                                     "price": {
#                                         "low": item_price,
#                                         "high": 0,
#                                         "unsigned": False,
#                                     },
#                                 },
#                                 "overrides": None,
#                             },
#                             "pricingPolicy": None,
#                         },
#                         "dishInfo": {
#                             "nutritionalInfo": {
#                                 "allergens": None,
#                                 "caloricInfo": None,
#                                 "jouleInfo": None,
#                             },
#                             "classifications": {
#                                 "cuisineUUID": None,
#                                 "mealTypeUUID": None,
#                                 "proteinTypeUUID": None,
#                                 "hasSide": None,
#                                 "isHot": None,
#                                 "isEntree": None,
#                                 "alcoholicItems": 0,
#                                 "hasAlcoholicItems": False,
#                                 "preparationType": None,
#                                 "drinkInfo": None,
#                                 "serviceType": None,
#                                 "foodInfo": None,
#                                 "classificationLabels": None,
#                                 "dietaryInfo": None,
#                                 "dietaryLabels": None,
#                                 "restrictedItem": None,
#                                 "gpcCode": None,
#                                 "packageKey": None,
#                                 "uberProductType": None,
#                                 "uberProductTraits": [],
#                                 "ingredients": None,
#                                 "additives": None,
#                                 "uberProductTypeV2": None,
#                             },
#                         },
#                         "customizationUUIDs": {
#                             "defaultValue": None,
#                             "overrides": None,
#                         },
#                         "suspensionInfo": {
#                             "defaultValue": {
#                                 "suspendUntil": "",
#                                 "suspendReason": "",
#                                 "suspendUntilMilliseconds": None,
#                             },
#                             "overrides": None,
#                         },
#                         "vendorInfo": {
#                             "externalID": "new_16406",
#                             "externalData": None,
#                             "groupUUID": None,
#                             "customizationTemplateUUID": None,
#                         },
#                         "tags": None,
#                         "quantityInfo": None,
#                         "taxLabelInfo": {
#                             "defaultValue": None,
#                         },
#                         "createdAt": "2023-08-05T23:51:18.517Z",
#                         "updatedAt": "2023-08-05T23:51:18.517Z",
#                         "visibility": None,
#                         "productInfo": {
#                             "externalProductIDType": None,
#                             "externalProductIDValue": None,
#                             "targetMarket": None,
#                         },
#                         "bundledItems": None,
#                         "attributeExtensions": {
#                             "dish_classification": {
#                                 "foodBusinessOperator": {
#                                     "address": None,
#                                 },
#                             },
#                             "beverage": {
#                                 "alcoholByVolume": {},
#                                 "caffeineAmount": {
#                                     "lower": {},
#                                     "upper": {},
#                                 },
#                                 "coffeeInfo": {},
#                             },
#                             "medication": {},
#                             "nutrition": {
#                                 "numberOfServingsInterval": {
#                                     "lower": {},
#                                     "upper": {},
#                                 },
#                                 "netQuantity": {
#                                     "decimalInterval": {
#                                         "lower": {},
#                                         "upper": {},
#                                     },
#                                     "unit": {},
#                                 },
#                                 "nutrientsList": [],
#                                 "servingSize": {
#                                     "decimalInterval": {
#                                         "lower": {},
#                                         "upper": {},
#                                     },
#                                     "unit": {},
#                                 },
#                                 "perServingCalories": None,
#                                 "perServingKilojoules": None,
#                             },
#                             "physical_properties": {},
#                             "price": {
#                                 "containerDeposit": {
#                                     "amountE5": {},
#                                 },
#                             },
#                             "product": {},
#                         },
#                         "sellingInfo": None,
#                         "metadata": None,
#                         "productUUID": None,
#                         "catalogIdentifiers": None,
#                         "taxInfo": {
#                             "taxRate": None,
#                             "vatRate": None,
#                         },
#                     },
#
#                     "menuType": "MENU_TYPE_FULFILLMENT_DELIVERY",
#                     "parentObjectUUIDs": [
#                         f"{category_uuid}",
#                     ],
#                 },
#             ],
#             "shouldLoadItems": True,
#             "cityId": 5,
#             "internalTags": [
#                 {
#                     "uuid": "ca4f2434-1a17-4691-b2cd-360cd0f4914d",
#                     "name": "createdbysfdc",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "2aac4591-ff7f-4940-a9ea-2bdde16e0e1d",
#                     "name": "post_pickle",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "f9fc75df-eb59-4847-8766-64edf10d3892",
#                     "name": "menu_maker_enabled",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "96e8d56c-7384-4769-9ecb-b48f32e00e62",
#                     "name": "enable_restaurant_alcohol_sales_hours",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "881330fb-d839-4972-b000-54e48eab080a",
#                     "name": "usc_ob_nv_reconciled",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "dfd9ccef-abce-4d18-a60c-8bd4f6efdd8c",
#                     "name": "alcohol_sku_verified",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "3f748007-ed6b-4038-999b-da430c87db94",
#                     "name": "alcohol_warning_sent_1",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "3e606252-d37d-4c40-ac43-ab67d9cc5e4c",
#                     "name": "houseads_q12023_xp",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "4f65488d-b743-46b7-96f4-fd431f6601ee",
#                     "name": "use_sections_as_categories",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "af538241-d266-44ad-9abf-7f7325cdbb1e",
#                     "name": "usc_visibility_tier_2",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "37fe3f48-e912-4724-a741-9bb87f6fb0e5",
#                     "name": "usc_quality_full_access",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#                 {
#                     "uuid": "3f4bbfcc-51c7-4966-ae13-0d26aa445ff5",
#                     "name": "has_restaurant_promotions",
#                     "type": "INTERNAL_TAG",
#                     "localizedName": None,
#                 },
#             ],
#             "countryCode": "US",
#             "storeUUID": "1a5ede99-3c38-5f9a-983f-2dc8c51988bb",
#         }
#         payload = str(json.dumps(json_data))
#
#         headers = {
#
#             'cookie': "sid=QA.CAESEAMp4aohmEYHsdwQTsUEvsYYysvapwYiATEqJGQwNGIwNjNkLTJlMmYtNDgyMS1hMjljLTAwZDMyYTU1M2QzMTJAuls0NXag8KIFUJF1KraVEIIYMPE22hjPzMqmaBHhUmonK9m52szMVeBU1WKVKag-TrvxL7YAMTgg9RkmZREjvjoBMUINLnViZXJlYXRzLmNvbQ.KVTtKa5MHi1KLy5XEAGOH-eXo2Hc1ELVQ_T9Mkp2E-8;",
#             'Host': "merchants.ubereats.com",
#             'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
#             'Accept': "*/*",
#             'Accept-Language': "en-US,en;q=0.5",
#             'Accept-Encoding': "gzip, deflate",
#             'Content-Type': "application/json",
#             'X-Csrf-Token': "x",
#             # 'Content-Length': "4157",
#             'Origin': "https://merchants.ubereats.com",
#             'Referer': f"https://merchants.ubereats.com/manager/menumaker/1a5ede99-3c38-5f9a-983f-2dc8c51988bb/overview?entityType=item&entityUUID={item_uuid}&mode=edit",
#             'Sec-Fetch-Dest': "empty",
#             'Sec-Fetch-Mode': "cors",
#             'Sec-Fetch-Site': "same-origin",
#             'Te': "trailers"
#             }
#
#         conn.request("POST", "/manager/menumaker/api/upsertMenus?localeCode=en", payload, headers)
#
#         res = conn.getresponse()
#         data = res.read()
#         print(item_name)
#

