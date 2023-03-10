from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Set up the OAuth 2.0 authorization flow
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=['https://www.googleapis.com/auth/gmail.readonly'])
creds = flow.run_local_server(port=0)
print(flow)
# Convert the credentials to a dictionary
creds_dict = {
    'client_id': creds.client_id,
    'client_secret': creds.client_secret,
    'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri
}

# Write the credentials to a JSON file
with open('credentials.json', 'w') as f:
    json.dump(creds_dict, f)
