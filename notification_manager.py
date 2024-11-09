
from twilio.rest import Client
class NotificationManager:
    def __init__(self):
        self.OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        self.api_key = "8e5c1f18afe5e44d22710ab81fac2a26"
        self.account_sid = "ACe2c7a5cc583497f91455de58881ae7dc"
        self.auth_token = "7c91c6db7a3011ca79a558f9071c8e40"
    def send_message(self,message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body= message,
            from_="+12407135498",
            to="+905389738050",
        )
        print(message.status)