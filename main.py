from googleapiclient.discovery import build
import pprint
import email_object
from email_auth import email_creds
from emailparser_MO import emailparser


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

EmailObject = email_object.EmailObject

def getEmails(index):

    creds = email_creds()

    service = build('gmail', 'v1', credentials=creds)

    result = service.users().messages().list(userId='me', labelIds=['Label_1031364781613739106'],
                                             maxResults=60).execute()

    messageId = result['messages'][index]['id']

    message = service.users().messages().get(userId='me', id=messageId).execute()

    payload = message['payload']
    headers = payload['headers']

    for header in headers:
        if header['name'] == 'Date':
            datetime = header['value']
        if header['name'] == 'From':
            sender = header['value']
        if header['name'] == 'Subject':
            subject = header['value']

    if sender == 'Missouri Courts eFiling System <mocourts.efiling@courts.mo.gov>':
        email_dict = emailparser(datetime,sender,subject,payload)
    else:
        email_dict = {
            'datetime': datetime,
            'sender': sender,
            'subject': subject,
            'ef_number': '',
            'plaintiff_name': '',
            'resident_1_name': '',
            'address': '',
        }

    return email_dict

new_email = EmailObject(getEmails(59))

pprint.pprint(vars(new_email))