import requests


def send_mail(token):

    with open("reports/members.html", "r") as f:
        html = f.read()

    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    email = {
        "message": {
            "subject": "Microsoft 365 Members Report",
            "body": {
                "contentType": "HTML",
                "content": html
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": "DavidKennedy@kennedycloudapp.onmicrosoft.com"
                    }
                }
            ]
        },
        "saveToSentItems": True
    }

    response = requests.post(
        "https://graph.microsoft.com/v1.0/users/DavidKennedy@kennedycloudapp.onmicrosoft.com/sendMail",
        headers=headers,
        json=email
    )

    print(response.status_code)

    if response.status_code == 202:
        print("Email sent successfully!")
    else:
        print(response.text)