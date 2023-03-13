
import pytest
from gmail_api import GmailService, GmailSender, GmailSearch

# Set up fixtures for creating instances of the GmailService, GmailSender, and GmailSearch classes
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

# Define test cases for sending emails and searching for messages
def test_send_email(sender):
    # Define parameters for sending a test email with an image attachment
    recipient = ['example1@gmail.com', 'example2@gmail.com']
    subject = 'Test Email'
    message_text = 'This is a test email sent using the Gmail API.'
    image_path = 'image.jpg'

    # Call the send_email method of the GmailSender class and check that it returns a message object
    message = sender.send_email(recipient, subject, message_text, image_path)
    assert message is not None

def test_send_email_no_image(sender):
    # Define parameters for sending a test email with no image attachment
    recipient = ['example1@gmail.com', 'example2@gmail.com']
    subject = 'Test Email'
    message_text = 'This is a test email sent using the Gmail API.'

    # Call the send_email method of the GmailSender class and check that it returns a message object
    message = sender.send_email(recipient, subject, message_text)
    assert message is not None

def test_search_messages(search):
    # Define a query for searching for messages from a specific email address
    query = 'from:example@gmail.com'

    # Call the search_messages method of the GmailSearch class and check that it returns a list of messages
    messages = search.search_messages(query)
    assert isinstance(messages, list)
    assert len(messages) >= 0
