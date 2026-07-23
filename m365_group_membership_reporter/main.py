from src.auth import get_token
from src.groups import get_groups
from src.display import print_member_summary
from src.exports import export_members
from src.html_report import create_member_html_report
from src.mailer_graph import send_mail
from src.members import get_members

token = get_token()

groups = get_groups(token)

for i, group in enumerate(groups, start=1):
    print(f"{i}. {group['displayName']}")
    print(f"     ID: {group['id']}")
    
choice = int(input("Select a group number: "))
selected_group = groups[choice -1]

group_id = selected_group["id"]
members = get_members(token, group_id)

print_member_summary(members)

# print_group_summary(groups)

export_members(members)

create_member_html_report(
    members,
    selected_group["displayName"],
    selected_group["mail"]
)

send_mail(token)


