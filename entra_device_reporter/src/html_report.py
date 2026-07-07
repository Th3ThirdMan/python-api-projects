def create_html_report(devices):
    with open("reports/entra_device_report.html", "w", encoding="utf-8") as f:
        f.write(f"""
<html>
<head>
<style>
body {{
    font-family: Arial;
    background-color: #f2f2f2;
    padding: 20px;
    max-width: 1000px;
    margin: auto;
}}

h1 {{
    background-color: #1f4e79;
    color: white;
    padding: 15px;
    border-radius: 5px;
}}

p {{
    font-size: 18px;
}}

.card {{
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    margin-top: 20px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background-color: white;
}}

th,
td {{
    border: 1px solid #cccccc;
    padding: 10px;
    text-align: left;
}}

th {{
    background-color: #1f4e79;
    color: white;
}}
</style>
</head>
<body>

<h1>Entra Device Report</h1>

<div class="card">
<p><strong>Total devices:</strong> {len(devices)}</p>
""")

        if len(devices) == 0:
            f.write("""
<p>No Entra devices found.</p>
""")
        else:
            f.write("""
<table>
<tr>
    <th>Device Name</th>
    <th>Operating System</th>
    <th>OS Version</th>
    <th>Trust Type</th>
</tr>
""")

            for device in devices:
                f.write(f"""
<tr>
    <td>{device.get("displayName")}</td>
    <td>{device.get("operatingSystem")}</td>
    <td>{device.get("operatingSystemVersion")}</td>
    <td>{device.get("trustType")}</td>
</tr>
""")

            f.write("""
</table>
""")

        f.write("""
</div>

</body>
</html>
""")
        
    return "reports/entra_device_report.html"