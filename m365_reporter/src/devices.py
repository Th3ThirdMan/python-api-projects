

import requests


def get_devices(token):
    endpoint = "https://graph.microsoft.com/v1.0/devices"

    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    print("Querying Microsoft Graph for devices...")

    response = requests.get(endpoint, headers=headers)

    data = response.json()

    devices = data["value"]
    
    print(f"Retrieved {len(devices)} devices")

    return devices