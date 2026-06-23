from src.auth import get_token
from src.users import get_users
from src.exports import export_summary, export_users
from src.summary import create_summary

token = get_token()

users = get_users(token)

count = export_users(users)

summary = create_summary(count, len(users), users)

export_summary(summary)

print(summary)

print(f"Licensed Users: {summary['licensed']}")
print(f"Total Users: {summary['total']}")
print(f"Unlicensed Users: {summary['unlicensed']}")
print(f"Percentage Licensed: {summary['percentage']}%")
print(f"Fully Licensed Tenant: {summary['fully_licensed']}")
print(f"Action Required: {summary['action_required']}")
print(f"Tenant Health: {summary['tenant_health']}")

