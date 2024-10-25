import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
load_dotenv(override=True)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ["OWM_API_KEY"]
account_sid = os.environ['TWILIO_ACC_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

weather_params = {
    "lat": 51.0501,
    "lon": -114.0853,
    "appid": api_key,
    "cnt": 4,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    elif int(condition_code) < 0:
        will_snow = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="+14155238886",
            to="+1403*******"
        )
    print(message.status)
