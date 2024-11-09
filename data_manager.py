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
