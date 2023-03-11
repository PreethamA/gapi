import os
import pytest
from gmail_api import GmailAPI


@pytest.fixture
def api():
    # Initialize the GmailAPI object using a test credentials file
    credentials_file = os.path.join(os.path.dirname(__file__), 'credentials.json')
    return GmailAPI(credentials_file)


def test_send_email(api):
    # Test sending an email
    message = api.send_email(recipient=['recipient1@example.com','recipient2@example.com'], subject='Test email', message_text='This is a test email.')
    assert message is not None


def test_search_messages(api):
    # Test searching for messages
    messages = api.search_messages(query='subject:example OR body:example')
    assert len(messages) > 0
