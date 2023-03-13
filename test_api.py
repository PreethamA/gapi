import pytest
import os
from gmail_api import GmailService, GmailSender, GmailSearch

creds_path = 'credentials.json'

@pytest.fixture
def service():
    return GmailService(creds_path).service

@pytest.fixture
def sender(service):
    return GmailSender(service)

@pytest.fixture
def search(service):
    return GmailSearch(service)

def test_send_email(sender):
    recipient = ['example1@gmail.com', 'example2@gmail.com']
    subject = 'Test Email'
    message_text = 'This is a test email sent using the Gmail API.'
    image_path = 'image.jpg'
    message = sender.send_email(recipient, subject, message_text, image_path)
    assert message is not None

def test_send_email_no_image(sender):
    recipient = ['example1@gmail.com', 'example2@gmail.com']
    subject = 'Test Email'
    message_text = 'This is a test email sent using the Gmail API.'
    message = sender.send_email(recipient, subject, message_text)
    assert message is not None

def test_search_messages(search):
    query = 'from:example@gmail.com'
    messages = search.search_messages(query)
    assert isinstance(messages, list)
    assert len(messages) >= 0
