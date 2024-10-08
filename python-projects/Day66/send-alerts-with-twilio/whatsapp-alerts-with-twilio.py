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
will_snow = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # Rain condition: weather condition codes 500-531
    if 500 <= int(condition_code) < 600:
        will_rain = True
    # Snow condition: weather condition codes 600-622
    elif 600 <= int(condition_code) < 700:
        will_snow = True

if will_rain or will_snow:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    if will_rain:
        message_body = "It's going to rain today. Remember to bring an ☔️"
    elif will_snow:
        message_body = "It's going to snow today. Stay warm and drive safe! ❄️☃️"

    message = client.messages \
        .create(
            body=message_body,
            from_="whatsapp:+14155238886",
            to="whatsapp:+1403*******"
        )
    print(f"Message sent: {message.status}")
