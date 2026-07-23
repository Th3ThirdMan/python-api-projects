# Microsoft 365 User Reporter

## Overview

A Python application that connects to Microsoft Graph to retrieve Microsoft 365 users, export them to CSV, generate an HTML report, and email the report using Microsoft Graph.

## Features

- Microsoft Graph authentication (MSAL)
- Retrieve Microsoft 365 users
- Console summary
- CSV export
- HTML report generation
- Email reports using Microsoft Graph

## Technologies

- Python
- Microsoft Graph API
- MSAL
- Requests
- python-dotenv

## Project Structure

main.py
src/
reports/

## How to Run

1. Clone the repository
2. Install requirements
3. Create a `.env`
4. Run `python3 main.py`

## Example Output

- users.csv
- users.html
- Email report
