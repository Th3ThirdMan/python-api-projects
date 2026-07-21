import csv


def export_users(users):
    with open("reports/users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "UPN", "Email", "Enabled"])
        
        for user in users:
            writer.writerow([
            user.get("displayName"),
            user.get("userPrincipalName"),
            user.get("mail"),
            user.get("accountEnabled")
        ])