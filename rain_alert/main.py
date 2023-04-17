import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "af829f94eae434efba38efc3f64685c2"
MY_LAT = 51.3180109
MY_LONG = 8.3062763


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=parameters)

response.raise_for_status()

data = response.json()

new_list = []

for item in data["list"]:
    new_list.append(item["weather"][0]["id"])

if new_list[0] < 700 or new_list[1] < 700:
    print("Raining")
else:
    print("Not raining")

