import requests

SHEET_USERS_ENDPOINT = 'https://api.sheety.co/9f3fc493610987355887eac26ad2f7d9/flightTracker/users'

print("Would you like to join Chris'Flight Club? \nWe find the best deals and email you")
firstName = input("What is your first name?")
lastName = input("What is your last name?")
email = input("What is your email?")
email_2 = input("Type your email again")
if email == email_2:
    print(firstName)
    new_data ={
    "user":{
            "firstName": firstName,
            "lastName": lastName,
            "email": email
        }
    }


    print(new_data)
    print(SHEET_USERS_ENDPOINT)
    response = requests.post(
        url=SHEET_USERS_ENDPOINT, json=new_data)
    print(response)

    print("You're in the club!")

