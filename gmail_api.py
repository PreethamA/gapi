from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os


class GmailAPI:
    def __init__(self, credentials_file):
        self.credentials = Credentials.from_authorized_user_file(credentials_file)
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def send_email(self, recipient, subject, message_text, image_path=None):
        # Create the message
        message = MIMEMultipart()
        message['to'] = ', '.join(recipient)
        message['subject'] = subject
        message.attach(MIMEText(message_text))

        # Add an image attachment
        if image_path:
            with open(image_path, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data, name=os.path.basename(image_path))
            message.attach(image)

        # Encode the message in base64
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Send the message
        try:
            message = self.service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
            print(f'Message Id: {message["id"]}')
        except HttpError as error:
            print(f'An error occurred: {error}')
            message = None
        return message

    def search_messages(self, query):
        # Search for messages containing a keyword in the subject or body
        response = self.service.users().messages().list(userId='me', q=query).execute()
        messages = response.get('messages', [])

        # Print the snippet of each matching message
        return messages


if __name__ == '__main__':
    # Initialize the GmailAPI object
    api = GmailAPI('credentials.json')

    # Send an email
    api.send_email(recipient=['recipient1@example.com', 'recipient2@example.com'], subject='Test email', message_text='This is a test email.')

    # Search for messages containing a keyword
    messages = api.search_messages(query='subject:example OR body:example')
    for message in messages:
        print(message['snippet'])
