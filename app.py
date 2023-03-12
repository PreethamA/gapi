from gmail_api import GmailAPI

api = GmailAPI('credentials.json')

# Send an email
api.send_email(recipient=['recipient1@example.com','recipient2@example.com'], subject='Test email', message_text='This is a test email.')

# Search for messages containing a keyword
messages = api.search_messages(query='subject:Test email')
for message in messages:
    print(message['snippet'])