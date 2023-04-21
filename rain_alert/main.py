import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = "ACcdf72bd085136fb1f6466fa8002c5bb4"
auth_token = os.environ.get("AUTH_TOKEN")
MY_LAT = 51.44083
MY_LONG = 5.47778



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=parameters)

response.raise_for_status()

data = response.json()

data = data["list"][:2]
new_list = []

for item in data:
    new_list.append(item["weather"][0]["id"])

if any(num < 700 for num in new_list):
    print("Raining")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+16206791233',
        body='It will rain, remember to bring an ☔️',
        to='+31629029783'
    )

    print(message.status)
else:
    print("Not raining")

