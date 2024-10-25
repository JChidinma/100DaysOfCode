import os
import json
import requests
import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(override=True)
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint)

        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response body: {response.text}")
            return None

        # Check for empty response
        if not response.text:
            print("Error: Empty response received")
            return None

        # Attempt to parse JSON response
        try:
            data = response.json()
            self.destination_data = data["prices"]
            # pprint(data)
            return self.destination_data
        except json.decoder.JSONDecodeError:
            print("Error: Failed to parse JSON from the response")
            print(f"Response body: {response.text}")
            return None

    # Make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
