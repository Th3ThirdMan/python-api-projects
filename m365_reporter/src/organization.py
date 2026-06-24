import requests

import requests


def get_organization(token):
    endpoint = "https://graph.microsoft.com/v1.0/organization"

    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    print("Querying Microsoft Graph for organization...")

    response = requests.get(endpoint, headers=headers)

    data = response.json()

    organization = data["value"]

    print(f"Retrieved {len(organization)} organization records")

    return organization