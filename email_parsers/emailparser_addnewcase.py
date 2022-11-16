import base64

def emailparserMO(messageId, datetime, sender, subject, payload):

    data = payload['parts'][0]['parts'][0]['parts'][0]['body']['data']
    data = data.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    decoded_data_string = str(decoded_data)
    ef_location = decoded_data_string.find('Your submission')
    ef_number = decoded_data_string[ef_location + 16:ef_location + 26]

    case_number_location = decoded_data_string.find('Case Number:')
    case_number = decoded_data_string[case_number_location + 13:case_number_location + 25]

    judge_location_start = decoded_data_string.find('assigned to Judge') + 18
    judge_location_end = decoded_data_string.find('and is scheduled') - 1
    judge = decoded_data_string[judge_location_start:judge_location_end]

    hearing_datetime_location = decoded_data_string.lower().find('in division')
    hearing_date = decoded_data_string[hearing_datetime_location - 20:hearing_datetime_location - 12]
    hearing_time = decoded_data_string[hearing_datetime_location - 9:hearing_datetime_location]

    return {
        'message_id': messageId,
        'datetime': datetime,
        'sender': sender,
        'subject': subject,
        'county': '',
        'ef_number': ef_number,
        'case_number': case_number,
        'plaintiff_name': '',
        'resident_1_name': '',
        'address': '',
        'judge': judge,
        'hearing_date': hearing_date,
        'hearing_time': hearing_time,
    }
