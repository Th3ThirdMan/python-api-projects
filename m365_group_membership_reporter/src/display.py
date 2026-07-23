
def print_member_summary(members):
    for member in members:
        print("--------------------")
        print(f"Name: {member.get('displayName')}")
        print(f"Email: {member.get('mail')}")
        print(f"ID: {member.get('id')}")
        print(f"User Principal Name: {member.get('userPrincipalName')}")
        