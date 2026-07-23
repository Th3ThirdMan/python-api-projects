import csv


def export_members(members):
    with open("reports/members.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "User Principal Name", "ID"])
        
        for member in members:
            writer.writerow([
            member.get("displayName"),
            member.get("mail"),
            member.get("userPrincipalName"),
            member.get("id")
        ])
            
            