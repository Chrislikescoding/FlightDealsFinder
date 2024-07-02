#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
cities=[]

dm=DataManager()
sheet_data=dm.get_destination_data()
fs=FlightSearch()
nm = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for item in sheet_data:

    iata_code = item['iataCode']
    print(iata_code)

    flight=fs.get_cheapest_price(iata_code)

    if flight is None:
        continue
    if item['lowestPrice'] > flight.price:
        users = dm.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        nm.send_emails(emails, message)

        #nm.send_message(
       # message=f"Low price alert! Only price to fly from {flight.origin_city} -{flight.origin_airport} to "
           #     f"{flight.destination_city} - {flight.destination_airport}from {flight.out_date} to {flight.return_date}")










