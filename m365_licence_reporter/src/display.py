


def print_user_summary(users):
    for user in users:
        print("--------------------")
        print(f"Name: {user.get('displayName')}")
        print(f"UPN: {user.get('userPrincipalName')}")
        print(f"Mail: {user.get('mail')}")
        print(f"Enabled: {user.get('accountEnabled')}")
        