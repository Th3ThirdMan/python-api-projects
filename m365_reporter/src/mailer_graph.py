import requests


def send_mail(token, user, html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    endpoint = f"https://graph.microsoft.com/v1.0/users/{user}/sendMail"

    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    email = {
        "message": {
            "subject": "M365 Tenant Report",
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
        }
    }
    
    response = requests.post(
        endpoint,
        headers=headers,
        json=email
    )
    
    print(response.status_code)