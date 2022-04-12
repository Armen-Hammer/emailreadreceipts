from flask import Flask, request, redirect
from twilio.rest import Client

import datetime
import os

account_sid = os.environ['account_sid']

# Your Auth Token from twilio.com/console
auth_token  = os.environ['token']

client = Client(account_sid, auth_token)

app = Flask(__name__)


@app.route('/log')
def log():
    """This will redirect to an image of a 1x1 transparent pixel. First it will send me message by text about the email that was opened before redirecting"""
    description = request.args.get("desc")

    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    if ip_addr in os.environ.get("protected_IPs", []): #useful for not sending messages if the request comes from a specific IP (eg... your own adress)
            return redirect("/static/1x1.png")

    message = client.messages.create(
            to=os.environ['to_number'], 
            from_=os.environ['from_number'],
            body=f"Email opened at {datetime.datetime.now().strftime('%m/%d/%Y %H:%M')}. Description: {description}. IP: {ip_addr}")

    return redirect("/static/1x1.png")


if __name__ == "__main__":
    app.run(debug=False)