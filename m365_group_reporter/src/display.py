


def print_group_summary(groups):
    for group in groups:
        print("--------------------")
        print(f"Name: {group.get('displayName')}")
        print(f"Mail: {group.get('mail')}")
        print(f"Mail Enabled: {group.get('mailEnabled')}")
        print(f"Security Enabled: {group.get('securityEnabled')}")
        print(f"Group Types: {group.get('groupTypes')}")
        