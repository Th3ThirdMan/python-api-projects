def create_member_html_report(members, group_name, group_email):

    # Start the HTML
    html = f"""
<html>
<head>
    <title>Microsoft 365 Members Report</title>
</head>
<body>
    <h1>Microsoft 365 Members Report</h1>
    <h2>Group: {group_name}</h2>
    <h3>Email: {group_email}</h3>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>User Principal Name</th>
            <th>ID</th>
        </tr>
"""

    # Add a row for each user
    for member in members:
        html += f"""
        <tr>
            <td>{member.get("displayName")}</td>
            <td>{member.get("mail")}</td>
            <td>{member.get("userPrincipalName")}</td>
            <td>{member.get("id")}</td>
        </tr>
"""

    # Finish the HTML
    html += """
    </table>
</body>
</html>
"""

    # Save the report
    with open("reports/members.html", "w") as f:
        f.write(html)
    