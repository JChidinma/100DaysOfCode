import os
import pprint
import requests
from dotenv import load_dotenv
load_dotenv(override=True)

API_Key = os.environ["API_KEY"]

# Correcting the URL by adding "http://" and removing extra spaces
url = "http://api.openweathermap.org/data/2.5/forecast?q=London,uk&APPID=6fb6978dc90f105132040405249d1267"
r = requests.get(url)
print(r.json())


class Weather:
    """


    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:

            # Use an f-string to insert city and API key properly
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError(
                "Provide either a city or latitude and longitude arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        # print(self.data)
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for dicty in self.data['list'][:4]:
            print(dicty)
            simple_data.append(
                (dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
            return simple_data
        # return (self.data['list'][0]['dt_txt'], self.data['list'][0]['main']['temp'], self.data['list'][0]['weather'][0]['description'])


# Creating a Weather instance for Calgary
# weather = Weather(apikey="6fb6978dc90f105132040405249d1267", city="Calgary")
weather = Weather(apikey="6fb6978dc90f105132040405249d1267",
                  city="Calgary", lat=51.0501, lon=-114.0853)

# print(weather.data)
# pprint.pprint(weather.next_12h())
pprint.pprint(weather.next_12h_simplified())
