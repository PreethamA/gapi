from gmail_api import GmailService, GmailSender, GmailSearch

# Path to credentials file
creds_path = 'credentials.json'

# Create a Gmail service instance
service = GmailService(creds_path).service

# Create a GmailSender instance
sender = GmailSender(service)

# Send an email
recipient = ['example1@gmail.com', 'example2@gmail.com']
subject = 'Test Email'
message_text = 'This is a test email sent using the Gmail API.'
sender.send_email(recipient, subject, message_text)

# Create a GmailSearch instance
search = GmailSearch(service)

# Search for messages
query = 'from:example1@gmail.com'
messages = search.search_messages(query)
print(f'Number of matching messages: {len(messages)}')
