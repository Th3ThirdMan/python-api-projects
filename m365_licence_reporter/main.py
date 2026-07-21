from src.auth import get_token
from src.users import get_users
from src.display import print_user_summary
from src.exports import export_users
from src.html_report import create_html_report
from src.mailer_graph import send_mail

token = get_token()

users = get_users(token)

print_user_summary(users)

export_users(users)

create_html_report(users)

send_mail(token)


