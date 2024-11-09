import requests
import json

class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/b4233df445ebd235db09302d7cfdcff0/flightDeals/prices"
        self.response = requests.get(self.url)
        self.data = self.response.json()

    def add_flight(self,city,price,code):
        data = {
            "City": city,
            "Lowest Price" : price,
            "IATA Code" : code
        }
        requests.post(self.url, json=data)

data = DataManager()
print(data.data)
#response = requests.get("https://api.sheety.co/b4233df445ebd235db09302d7cfdcff0/flightDeals/prices")
#flights = response.json()
#print(flights)
#for city in flights["prices"]:
#    cities = city["city"]
#    ids = city["id"]
#    prices = city["lowestPrice"]
#    params = {
#      "keyword": cities
#    }
#    headers = {
#      "Authorization": "Bearer iYU2Oz7S2jckYgBxJyelJKhsAs8n"
#    }
#    response1 = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities", params=params,
#                            headers=headers)
#    code = response1.json()
#    codes = code["data"][0]["iataCode"]
#    data = {
#      "price": {
#      "iataCode" : codes
#    }
#    }
#    putting = requests.put(f"https://api.sheety.co/b4233df445ebd235db09302d7cfdcff0/flightDeals/prices/{ids}",json=data)
#    print(putting.text)