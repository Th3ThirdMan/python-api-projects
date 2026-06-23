import requests

def get_groups(token):
    endpoint = "https://graph.microsoft.com/v1.0/groups?$select=displayName, id"
    
    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }
    
    print("Querying Microsoft Graph for groups...")
    
    response = requests.get(endpoint, headers=headers)

    data = response.json()

    groups = data["value"]

    print(f"Retrieved {len(groups)} groups")

    return groups