import requests

def get_groups(token):
    endpoint = ("https://graph.microsoft.com/v1.0/groups"
                "?$select=displayName,mail,mailEnabled,securityEnabled,groupTypes"
    )


    headers = {
        "Authorization": f"Bearer {token['access_token']}"
    }

    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json().get("value", [])
    print(f"Graph request failed: {response.status_code}")
    print(response.text)
    return []