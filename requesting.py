import json
import requests


def getin(number):
        url = "https://gateway-staging.ncrcloud.com/catalog/item-prices/"+str(number)+"/1"

        headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'nep-application-key': "8a0287d86613f80201664703de9d0020",
            'nep-organization': "ncr-market",
            'nep-enterprise-unit': "7c54465e9f5344598276ec1f941f5a3c",
            'nep-service-version': "2.2.1:2",
            'Authorization': "Basic YWNjdDp5YWNrZXRzQHlhY2tldHNzZXJ2aWNldXNlcjpoYWNrZ3N1MjAxOA==",
            'Cache-Control': "no-cache",
            'Postman-Token': "8ad9aabc-1194-485e-9b62-e1f4deccd45d",
            'Username': "acct:yackets@yacketsserviceuser",
            'Password': "hackgsu2018"
            }

        response = requests.request("GET", url, headers=headers)
        response1 = response.json()

        return response1['price']


def order2(payloaded):
        url = "https://gateway-staging.ncrcloud.com/order/orders"

        payload = payloaded

        headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'nep-application-key': "8a0287d86613f80201664703de9d0020",
            'nep-service-version': "3.0.0:1",
            'Authorization': "Basic YWNjdDp5YWNrZXRzQHlhY2tldHNzZXJ2aWNldXNlcjpoYWNrZ3N1MjAxOA==",
            'Cache-Control': "no-cache",
            'Postman-Token': "f9af5c87-e2db-42f4-a6a5-de88eb066415",
            'Username': "acct:yackets@yacketsserviceuser",
            'Password': "hackgsu2018"
        }




        response = requests.post(url, payload , headers=headers)
        print(response.text)
