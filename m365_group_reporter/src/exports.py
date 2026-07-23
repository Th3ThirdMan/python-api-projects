import csv


def export_groups(groups):
    with open("reports/groups.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Mail Enabled", "Security Enabled", "Types"])
        
        for group in groups:
            writer.writerow([
            group.get("displayName"),
            group.get("mail"),
            group.get("mailEnabled"),
            group.get("securityEnabled"),
            group.get("groupTypes")
        ])
            
            