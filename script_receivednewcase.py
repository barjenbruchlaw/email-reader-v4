from googleapiclient.discovery import build
import pprint
import email_object
import sys
from email_auth import email_creds
from email_parsers.emailparser_receivednewcase import emailparserMO, emailparserKS, emailparserJOCO

sys.path.append('./email_parsers')

EmailObject = email_object.EmailObject

def getEmails(index):

    creds = email_creds()

    service = build('gmail', 'v1', credentials=creds)

    result = service.users().messages().list(userId='me', labelIds=['Label_1031364781613739106'],
                                             maxResults=100).execute()

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
        email_dict = emailparserMO(messageId,datetime,sender,subject,payload)
    elif sender == '<ks_efile_noreply@kscourts.org>':
        email_dict = emailparserKS(messageId,datetime,sender,subject,payload)
    elif sender == 'jococourts@jocogov.org':
        email_dict = emailparserJOCO(messageId,datetime, sender, subject, payload)
    else:
        email_dict = {
            'message_id': messageId,
            'datetime': datetime,
            'sender': sender,
            'subject': subject,
            'ef_number': '',
            'plaintiff_name': '',
            'resident_1_name': '',
            'address': '',
        }

    return email_dict

new_email = EmailObject(getEmails(15))

pprint.pprint(vars(new_email))