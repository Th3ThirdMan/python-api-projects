import requests


def send_mail(token, user):
    endpoint = f"https://graph.microsoft.com/v1.0/users/{user}/sendMail"

    print(endpoint)

    return endpoint