import requests

def get_users(token):
    endpoint = "https://graph.microsoft.com/v1.0/users?$select=displayName,userPrincipalName,assignedLicenses"
    
    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    print(f"Calling {endpoint}")

    print("Querying Microsoft Graph...")

    response = requests.get(endpoint, headers=headers)

    data = response.json()

    users = data["value"]

    print("Response received")
    print(f"Retrieved {len(users)} users")

    return users  