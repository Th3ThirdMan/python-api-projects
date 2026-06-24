from src.groups import get_groups
from src.auth import get_token
from src.users import get_users
from src.exports import export_summary, export_users
from src.summary import create_summary
from src.licences import get_licences
from src.organization import get_organization
from src.display import print_tenant_summary


token = get_token()

users = get_users(token)

groups = get_groups(token)

licences = get_licences(token)

organization = get_organization(token)

count = export_users(users)

summary = create_summary(count, len(users), users)

export_summary(summary)

print_tenant_summary(
    summary,
    groups,
    licences,
    organization
)