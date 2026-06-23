import csv


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

def export_summary(summary):
    with open("m365_reporter/m365_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Metric", "Value"])
        
        for key, value in summary.items():
            writer.writerow([key, value])