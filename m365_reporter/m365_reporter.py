import csv
import json
import requests
from msal import ConfidentialClientApplication

    
def get_users(token):
    endpoint = "https://graph.microsoft.com/v1.0/users?$select=displayName,userPrincipalName,assignedLicenses"
    
    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json"
    }

    print(f"Calling {endpoint}")
    print("headers")

    print("Sending request...")

    response = requests.get(endpoint, headers=headers)

    data = response.json()

    users = data["value"]

    print("Response received")
    print(f"Retrieved {len(users)} users")

    return users    
    
    

def get_token():

    tenant_id = "43ce61cb-56d1-470e-aca5-4aa763e5280a"
    client_id = "b30c59da-2b84-4979-a94d-b69bfd4a4040"
    client_secret = "PASTE_SECRET_HERE"
        
    app = ConfidentialClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret
    )
        
    token = app.acquire_token_for_client(
        scopes = ["https://graph.microsoft.com/.default"]
    )
    
    return token


def export_users(users):
    with open("m365_reporter/m365_users.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "UPN", "Licensed", "License Count"])

        licensed_count = 0

        for user in users:
            if user["assignedLicenses"]:
                licensed = "Yes"
                licensed_count += 1
            else:
                licensed = "No"

            license_count = len(user["assignedLicenses"])

            writer.writerow([
                user["displayName"],
                user["userPrincipalName"],
                licensed,
                license_count
            ])

    return licensed_count


def create_summary(licensed_count, total_users):
    summary = {
        "licensed": licensed_count,
        "total": total_users,
        "unlicensed": total_users - licensed_count,
        "percentage": round((licensed_count / total_users) * 100, 2),
        "fully_licensed": licensed_count == total_users,
        "action_required": licensed_count < total_users,
        "average_licences_per_user": round(
            sum(len(user["assignedLicenses"]) for user in users)
            / total_users,
            2
        ),
        "tenant_health":
    "Good"
    if licensed_count / total_users >= 0.9
    else "Needs Attention"
    }

    return summary

def export_summary(summary):
    with open("m365_reporter/m365_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Metric", "Value"])
        
        for key, value in summary.items():
            writer.writerow([key, value])

token = get_token()

users = get_users(token)

count = export_users(users)

summary = create_summary(count, len(users))

export_summary(summary)

print(summary)

print(f"Licensed Users: {summary['licensed']}")
print(f"Total Users: {summary['total']}")
print(f"Unlicensed Users: {summary['unlicensed']}")
print(f"Percentage Licensed: {summary['percentage']}%")
print(f"Fully Licensed Tenant: {summary['fully_licensed']}")
print(f"Action Required: {summary['action_required']}")
print(f"Tenant Health: {summary['tenant_health']}")

