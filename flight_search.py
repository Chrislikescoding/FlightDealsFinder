from pprint import pprint
import requests
import datetime as dt
from flight_data import FlightData
import prettyprint

TEQUILA_API_KEY = 'QWKWSzZRLWnpjy9eMUtuTMb2-bQ9pS11'
TEQUILA_ENDPOINT='https://api.tequila.kiwi.com/locations/query'
KIWI_SEARCH_ENDPOINT='https://api.tequila.kiwi.com/v2/search?'
BOOKING_TOKEN_API_KEY = 'LvSEtzUmgrfZdBtjVuGCU8XibHHseyv6'

# This class is responsible for talking to the Flight Search API.
class FlightSearch():

    def get_iatacode(self, city):
        header = {
            'apikey': TEQUILA_API_KEY
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}?term={city}&location_types=airport&active_only=true",
            headers=header)
        iataCode = response.json()['locations'][0]['city']['code']

        return iataCode

    def get_cheapest_price(self, fly_to, fly_from="LON", num_of_months=6, currency="GBP"):
        tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d/%m/%Y')
        six_months_time = (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y')

        header = {
            'apikey': BOOKING_TOKEN_API_KEY
        }
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": tomorrow,
            "date_to": six_months_time,
            "curr": currency,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "sort": "price",
            "limit": 1,
            "via_city":" "

        }

        flight_exist = False
        i=0
        while flight_exist == False and i < 2:
            try:
                response = requests.get(url=KIWI_SEARCH_ENDPOINT, headers=header, params=params)
                data=response.json()["data"][0]
              #  pprint(response.json())
            except IndexError:
                print(f"Flight data does not exist for {fly_to}, {i} stopovers")

                params.update({"max_stopovers": i})
                i+=1
            else:
                flight_exist = True

        if flight_exist:
            if i>0:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0])

            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs = 1,
                    via_city = data["route"][0]["cityTo"]
                    )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data





