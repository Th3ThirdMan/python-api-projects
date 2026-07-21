def create_html_report(users):

    # Start the HTML
    html = """
<html>
<head>
    <title>Microsoft 365 Users</title>
</head>
<body>
    <h1>Microsoft 365 User Report</h1>

    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Enabled</th>
        </tr>
"""

    # Add a row for each user
    for user in users:
        html += f"""
        <tr>
            <td>{user["displayName"]}</td>
            <td>{user["mail"]}</td>
            <td>{user["accountEnabled"]}</td>
        </tr>
"""

    # Finish the HTML
    html += """
    </table>
</body>
</html>
"""

    # Save the report
    with open("reports/users.html", "w") as f:
        f.write(html)
    