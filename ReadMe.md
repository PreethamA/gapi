
Steps to setup test gmail account and enable the API for sending and searching messages

Create a new Gmail API project:
1. Go to https://console.developers.google.com create an account and sign in with your Google account.
2. Create a new project by clicking on the "Select a project" drop-down menu on the top bar and then click on the "New project" button. Follow the prompts to create the project and give it a name.
3. Once the project is created, go to the project dashboard by clicking on the project name in the drop-down menu on the top bar.
4. Click on the "Enable APIs and Services" button on the dashboard page.
5. Search for "Gmail API" in the search bar and select it. 
6. Click on the "Enable" button to enable the Gmail API for your project. 


Set up authentication:

7. Next, you will need to create OAuth 2.0 credentials for your project so that it can authenticate and access your Gmail account. To do this, click on the "Create credentials" button and select "OAuth client ID". 
8. Choose "Desktop App" as the application type and give it a name. 
9. Click on the "Create" button to create the credentials. 
10. On the next screen, you will see your client ID and client secret. Click on the "Download" button to download your credentials as a JSON file. 


Install the Google API client library and test of features(send_email and search message):


11. Install the python packages from requirements.txt file
12. Once you have your credentials and python packages installed, the gmail_api.py file contains GMAILAPI class
    with methods send_email and search_messages to send email and search for specific messages in your mailbox
13. app.py file contains to create object of GMAILAPI class  to send email and search message 
14. test_api.py file contains test cases for the GMAILAPI class member functions
