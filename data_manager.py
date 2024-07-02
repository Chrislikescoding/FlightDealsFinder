from pprint import pprint

import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/9f3fc493610987355887eac26ad2f7d9/flightTracker/sheet1'
SHEET_USERS_ENDPOINT = 'https://api.sheety.co/9f3fc493610987355887eac26ad2f7d9/flightTracker/users'
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
            )
            print(response.text)

