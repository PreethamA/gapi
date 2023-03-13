from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
import os

class GmailService:
    def __init__(self, credentials_file):
        self.credentials = Credentials.from_authorized_user_file(credentials_file)
        self.service = build('gmail', 'v1', credentials=self.credentials)

class GmailSender:
    def __init__(self, service):
        self.service = service

    def send_email(self, recipient: list[str], subject: str, message_text: str, image_path:str=None):
        '''
        :param recipient: recipient email list
        :param subject: subject name of the email
        :param message_text: message to send
        :param image_path: atttahchments to add if any
        :return: JSON object, includes message id, threadId,labelIds,snippet, historyId and payload
        '''
        # Create the message
        message = MIMEMultipart()
        message['to'] = ','.join(recipient)
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

class GmailSearch:
    def __init__(self, service):
        self.service = service

    def search_messages(self, query: str):
        '''

        :param query: text
        :return: JSON object, includes message id, threadId
        '''
        # Search for messages containing a keyword in the subject or body
        response = self.service.users().messages().list(userId='me', q=query).execute()
        messages = response.get('messages', [])

        # Print the snippet of each matching message
        return messages




