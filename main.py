from googleapiclient.discovery import build
import base64
import pprint
import email_object_MO
from email_auth import email_creds


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

EmailObject = email_object_MO.EmailObject_MO

def getEmails(index):

    creds = email_creds()

    service = build('gmail', 'v1', credentials=creds)

    result = service.users().messages().list(userId='me', labelIds=['Label_1031364781613739106'],
                                             maxResults=20).execute()

    messageId = result['messages'][index]['id']

    message = service.users().messages().get(userId='me', id=messageId).execute()

    payload = message['payload']
    headers = payload['headers']
    data = payload['parts'][0]['parts'][0]['parts'][0]['body']['data']

    data = data.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    decoded_data_string = str(decoded_data)

    for header in headers:
        if header['name'] == 'Date':
            datetime = header['value']
        if header['name'] == 'From':
            sender = header['value']
        if header['name'] == 'Subject':
            subject = header['value']

    ef_location = decoded_data_string.find('Filing Confirmation Number')
    ef_number = decoded_data_string[ef_location + 28:ef_location + 38]

    plaintiff_name_location_start = decoded_data_string.find(
        'After that time, you will have to login to Case.net and use the') + 133
    plaintiff_name_location_end = decoded_data_string.find('Party Type:') - 8

    plaintiff_name = decoded_data_string[plaintiff_name_location_start:plaintiff_name_location_end]

    defendant_info_index = decoded_data_string.find("Party Type: Defendant")
    defendant_info_start = defendant_info_index - 50
    defendant_info_end = defendant_info_index + 150
    defendant_info = decoded_data_string[defendant_info_start:defendant_info_end]
    resident_1_name_start = defendant_info.find("Filer") + 16
    resident_1_name_end = defendant_info.find("Party Type") - 8
    resident_1_name = defendant_info[resident_1_name_start:resident_1_name_end]
    address_start = defendant_info.find("Address:") + 9
    address_end = defendant_info.find("SSN/EIN:") - 9
    address = defendant_info[address_start:address_end]

    return {
        'datetime': datetime,
        'sender': sender,
        'subject': subject,
        'ef_number': ef_number,
        'plaintiff_name': plaintiff_name,
        'resident_1_name': resident_1_name,
        'address': address,
    }


new_email = EmailObject(getEmails(4))

pprint.pprint(vars(new_email))