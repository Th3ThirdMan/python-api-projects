
def create_html_report(summary, groups, licences, organization, devices):
    org = organization[0]
    domain = org["verifiedDomains"][0]

    html = f"""
<html>

<head>

<style>

body {{
    font-family: Arial;
    background-color: #f4f6f9;
    padding: 20px;
    max-width: 1000px;
    margin: auto;
}}

p {{
    font-size: 18px;
}}

h1 {{
    background-color: #1f4e79;
    color: white;
    padding: 15px;
}}

h2 {{
    color: #1f4e79;
}}

.card {{
    background-color: white;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    transition: 0.3s;
}}

.card:hover {{
    transform: translateY(-2px);
}}

.good {{
    color: green;
}}

.bad {{
    color: red;
}}

</style>

</head>

<body>

<h1>M365 Tenant Report</h1>

<div class="card">
<h2>Organization</h2>
<p>Name: {org["displayName"]}</p>
<p>Domain: {domain["name"]}</p>
<p>Type: {domain["type"]}</p>
</div>

<div class="card">
<h2>Users</h2>
<p>Total: {summary["total"]}</p>
<p>Licensed: {summary["licensed"]}</p>
<p>Unlicensed: {summary["unlicensed"]}</p>
</div>

<div class="card">
<h2>Groups</h2>
<p>Total: {len(groups)}</p>
</div>

<div class="card">
<h2>Licences</h2>
<p>Total SKUs: {len(licences)}</p>
</div>

<div class="card">
<h2>Devices</h2>
<p>Total: {len(devices)}</p>
</div>

<div class="card">
<h2>Health</h2>

<p class="{'good' if summary['tenant_health']=='Good' else 'bad'}">
{summary["tenant_health"]}
</p>

</div>

</body>

</html>

"""

    with open("m365_reporter/reports/tenant_report.html", "w") as file:
        file.write(html)