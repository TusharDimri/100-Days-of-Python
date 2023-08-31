import os
from twilio.rest import Client

account_sid = "ACd2de146f313d32bafaadb8fce79f1181"
auth_token = "75e14a8577cfc8f74fb24cb0b727b8d3"

client = Client(account_sid, auth_token)


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def sendNotification(self, **qwargs):
        msg = f"Lowest Price Alert! Only £{qwargs['price']} to fly from {qwargs['cityFrom']}-{qwargs['flyFrom']} to {qwargs['cityTo']}-{qwargs['flyTo']}, from {qwargs['departure_date']} to {qwargs['arrival_date']}"
        message = client.messages.create(
        body=msg,
        from_="+15856485982",
        to="+917983716823"
        )
        print(message.sid)
