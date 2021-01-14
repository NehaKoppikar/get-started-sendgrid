import sendgrid
import schedule
import time
from creds import key, from_email, to_email

sg = sendgrid.SendGridAPIClient(api_key=key)
data = {
    "personalizations": [
        {
            "to": [
                {
                    "email": to_email
                }
            ],
            "subject": "Sending with SendGrid is Fun"
        }
    ],
    "from": {
        "email": from_email
    },
    "content": [
        {
            "type": "text/plain",
            "value": "Good Morning"
        }
    ]
}

def send_email():
    response = sg.client.mail.send.post(request_body=data)

response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

schedule.every().day.at("07:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(2)
