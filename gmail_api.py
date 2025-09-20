import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


def send_email(to: list[str], subject: str, body: str):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials/gmail_cred.json',
        SCOPES
    )

    creds = flow.run_local_server()

    service = build('gmail', 'v1', credentials=creds)


    for address in to:
        
        message = MIMEText(body)
        message['subject'] = subject
        message['to'] = address
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = service.users().messages().send(userId='me', body=create_message).execute()
            print(f'Sent message to {message}, message Id: {message['id']}')
        except HTTPError as e:
            print(f'An error has occured: {e}')