def create_html_report(groups):

    # Start the HTML
    html = """
<html>
<head>
    <title>Microsoft 365 Group Report</title>
</head>
<body>
    <h1>Microsoft 365 Group Report</h1>

    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Mail Enabled</th>
            <th>Security Enabled</th>
            <th>Types</th>
        </tr>
"""

    # Add a row for each user
    for group in groups:
        html += f"""
        <tr>
            <td>{group["displayName"]}</td>
            <td>{group["mail"]}</td>
            <td>{group["mailEnabled"]}</td>
            <td>{group["securityEnabled"]}</td>
            <td>{group["groupTypes"]}</td>
        </tr>
"""

    # Finish the HTML
    html += """
    </table>
</body>
</html>
"""

    # Save the report
    with open("reports/groups.html", "w") as f:
        f.write(html)
    