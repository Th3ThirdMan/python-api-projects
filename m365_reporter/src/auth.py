import os
from dotenv import load_dotenv
from msal import ConfidentialClientApplication


def get_token():

    load_dotenv("m365_reporter/.env")
    
    tenant_id = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
        
    app = ConfidentialClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret
    )
        
    token = app.acquire_token_for_client(
        scopes = ["https://graph.microsoft.com/.default"]
    )
    
    return token