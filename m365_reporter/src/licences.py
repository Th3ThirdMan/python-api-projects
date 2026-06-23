import requests

def get_licences(token):
    endpoint = "https://graph.microsoft.com/v1.0/subscribedSkus"

    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    print("Querying Microsoft Graph for licences...")

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    licences = data["value"]

    print(f"Retrieved {len(licences)} licence SKUs")

    return licences