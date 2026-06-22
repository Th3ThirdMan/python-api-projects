import csv


users = [
    {
        "displayName": "David Kennedy",
        "userPrincipalName": "david@contoso.com",
        "assignedLicenses": [{"skuId": "abc123"}]
    },
    {
        "displayName": "John Smith",
        "userPrincipalName": "john@contoso.com",
        "assignedLicenses": []
    },
    {
        "displayName": "Sarah Jones",
        "userPrincipalName": "sarah@contoso.com",
        "assignedLicenses": [
            {"skuId": "xyz789"},
            {"skuId": "abc456"}
        ]
    }
]


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

