from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def prepare_email_report(recipient, subject, html_path):
    print("Preparing email report...")

    with open(html_path, "r") as file:
        html_content = file.read()

    message = MIMEMultipart()

    message["To"] = recipient
    message["Subject"] = subject

    message.attach(
        MIMEText(html_content, "html")
    )
    
    print("Connecting to SMTP...")

    server = smtplib.SMTP("smtp.office365.com", 587)

    print(server)

    server.quit()