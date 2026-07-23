from src.auth import get_token
from src.groups import get_groups
from src.display import print_group_summary
from src.exports import export_groups
from src.html_report import create_html_report
from src.mailer_graph import send_mail

token = get_token()

groups = get_groups(token)

print_group_summary(groups)

export_groups(groups)

create_html_report(groups)

send_mail(token)


