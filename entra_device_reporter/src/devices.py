import requests


def get_devices(token):
    endpoint = "https://graph.microsoft.com/v1.0/devices"

    headers = {
        "Authorization": f"Bearer {token['access_token']}"
    }

    response = requests.get(endpoint, headers=headers)
    print(response.status_code)
    print(response.text)

    return response.json().get("value", [])