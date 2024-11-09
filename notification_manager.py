
from twilio.rest import Client
class NotificationManager:
    def __init__(self):
        self.OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        self.api_key = "your key"
        self.account_sid = "your sid"
        self.auth_token = "your token"
    def send_message(self,message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body= message,
            from_="+number",
            to="+number",
        )
        print(message.status)
