from src.groups import get_groups
from src.auth import get_token
from src.users import get_users
from src.exports import export_summary, export_users
from src.summary import create_summary
from src.licences import get_licences
from src.organization import get_organization
from src.display import print_tenant_summary
from src.devices import get_devices
from src.html_report import create_html_report
from src.mailer import prepare_email_report
from src.mailer_graph import send_mail



token = get_token()

users = get_users(token)

groups = get_groups(token)

licences = get_licences(token)

organization = get_organization(token)

devices = get_devices(token)

count = export_users(users)

summary = create_summary(count, len(users), users)

export_summary(summary)

print_tenant_summary(
    summary,
    groups,
    licences,
    organization,
    devices
)

create_html_report(
    summary,
    groups,
    licences,
    organization,
    devices
)

send_mail(
    token,
    users[0]["userPrincipalName"]
)