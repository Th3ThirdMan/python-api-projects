import requests

def get_members(token, group_id):
    endpoint = (f"https://graph.microsoft.com/v1.0/groups/{group_id}/members"
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