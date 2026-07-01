# M365 Reporter

## Overview

M365 Reporter is a Python application that authenticates with Microsoft Graph and generates reports about a Microsoft 365 tenant.

The application retrieves tenant information, users, groups, licences and devices before exporting the data to CSV, generating an HTML report and emailing the report using Microsoft Graph.

---

## Features

- Microsoft Graph authentication (OAuth2)
- User reporting
- Group reporting
- Licence reporting
- Device reporting
- CSV exports
- HTML report generation
- Email report using Microsoft Graph

---

## Technologies

- Python
- Microsoft Graph API
- MSAL
- Requests
- HTML
- CSV

---

## Requirements

- Python 3.13+
- Microsoft 365 tenant
- Entra App Registration
- Client ID
- Tenant ID
- Client Secret

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file containing:

```text
TENANT_ID=
CLIENT_ID=
CLIENT_SECRET=
```

---

## Run

```bash
python3 m365_reporter/main.py
```

---

## Output

The application:

- Retrieves Microsoft 365 tenant information
- Generates CSV reports
- Generates an HTML report
- Sends the report by email using Microsoft Graph

---

## Future Improvements

- User table in HTML report
- Licence breakdown
- Sign-in activity
- Device compliance
- Dashboard charts
- Scheduled reporting
