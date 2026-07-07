from src.auth import get_token
from src.devices import get_devices
from src.display import print_device_summary
from src.exports import export_devices
from src.html_report import create_html_report
from src.mailer_graph import send_mail

token = get_token()
devices = get_devices(token)

print_device_summary(devices)
export_devices(devices)

html_report_path = create_html_report(devices)

user = "DavidKennedy@kennedycloudapp.onmicrosoft.com"

send_mail(
    token,
    user,
    html_report_path
)