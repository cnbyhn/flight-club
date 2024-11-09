import requests
import json
from datetime import datetime, timedelta

from data_manager import DataManager

class FlightSearch:
    def __init__(self, data_manager: DataManager):
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.origin = "ADB"
        self.flight_data = data_manager
        self.cheapest_flights = {}

    def search(self):
        current_date = datetime.now()
        API_KEY = "gu5miwNWKPx7Mfs5vHjv97N3wsUpG5EK"
        API_SECRET = "b7W7TowJHFuLekBh"
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        # Get access token
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET
        }
        response = requests.post(token_url, data=token_data)
        access_token = response.json().get('access_token')

        if not access_token:
            print(f"Failed to retrieve access token: {response.status_code} - {response.text}")
            return json.dumps({"error": "Failed to retrieve access token"})


        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }


        start_date = (current_date + timedelta(days=7)).strftime("%Y-%m-%d")  # Start date 7 days from now


        for dest in self.flight_data.data["prices"]:
            dest_code = dest["iataCode"]


            params = {
                "currencyCode": "USD",
                "originDestinations": [
                    {
                        "id": "1",
                        "originLocationCode": self.origin,
                        "destinationLocationCode": dest_code,
                        "departureDateTimeRange": {
                            "date": start_date,
                            "dateWindow": "P3D"
                        }
                    }
                ],
                "travelers": [
                    {
                        "id": "1",
                        "travelerType": "ADULT"
                    }
                ],
                "sources": ["GDS"],
                "max": 10
            }


            flights_response = requests.post(search_url, json=params, headers=headers)

            if flights_response.status_code == 200:
                flights_data = flights_response.json()
                if "data" in flights_data:
                    for flight in flights_data["data"]:
                        total_price = float(flight["price"]["total"])


                        if dest_code not in self.cheapest_flights:

                            self.cheapest_flights[dest_code] = {
                                "price": total_price,
                                "itineraries": flight["itineraries"]
                            }
                        else:

                            if total_price < self.cheapest_flights[dest_code]["price"]:
                                self.cheapest_flights[dest_code] = {
                                    "price": total_price,
                                    "itineraries": flight["itineraries"]
                                }
            else:
                print(f"Error retrieving flights for {start_date}: {flights_response.status_code} - {flights_response.text}")


        return json.dumps(self.cheapest_flights)




