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

def emailparserKS(messageId, datetime, sender, subject, payload):
    data = payload['body']['data']
    data = data.replace("-","+").replace("_","/")
    decoded_data = base64.b64decode(data)
    decoded_data_string = str(decoded_data)

    case_number_location = decoded_data_string.find('RE:')
    case_number = decoded_data_string[case_number_location + 4:case_number_location + 18]

    county_location_start = decoded_data_string.find('DISTRICT COURTS') + 46
    county_location_end = decoded_data_string.find('County') - 1
    county = decoded_data_string[county_location_start:county_location_end]

    judge_location_start = decoded_data_string.find('Judge') + 25
    judge_location_end = decoded_data_string.find('Division') - 2
    judge = decoded_data_string[judge_location_start:judge_location_end]

    caption_start = decoded_data_string.find('Case Title:') + 24
    caption_end = decoded_data_string.find('Document(s) Submitted:') - 40
    caption = decoded_data_string[caption_start:caption_end]
    versus_location = caption.find('vs.')
    plaintiff_name = caption[0:versus_location - 1]
    resident_1_name = caption[versus_location + 4:]

    return {
        'message_id': messageId,
        'datetime': datetime,
        'sender': sender,
        'subject': subject,
        'county': county,
        'ef_number': '',
        'case_number': case_number,
        'plaintiff_name': plaintiff_name,
        'resident_1_name': resident_1_name,
        'address': '',
        'judge': judge,
        'hearing_date': '',
        'hearing_time': '',
    }

def emailparserJOCO(messageId, datetime, sender, subject, payload):
    data = payload['body']['data']
    data = data.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    decoded_data_string = str(decoded_data)

    ef_location = decoded_data_string.find('E-filing')
    ef_number = decoded_data_string[ef_location + 9:ef_location + 19]

    plaintiff_location_start = decoded_data_string.find("for new case") + 13
    plaintiff_location_end = decoded_data_string.find('vs') - 1
    plaintiff_name = decoded_data_string[plaintiff_location_start:plaintiff_location_end]

    resident_1_location_start = decoded_data_string.find('vs') + 3
    resident_1_location_end = decoded_data_string.find('has been accepted') - 1
    resident_1_name = decoded_data_string[resident_1_location_start:resident_1_location_end]

    case_number_location = decoded_data_string.find('given case number')
    case_number = decoded_data_string[case_number_location + 18:case_number_location + 27]

    judge_start = decoded_data_string.find('to Judge') + 9
    judge_end = decoded_data_string.find('in Division') - 1
    judge = decoded_data_string[judge_start:judge_end]

    return {
        'message_id': messageId,
        'datetime': datetime,
        'sender': sender,
        'subject': subject,
        'county': 'Johnson',
        'ef_number': ef_number,
        'case_number': case_number,
        'plaintiff_name': plaintiff_name,
        'resident_1_name': resident_1_name,
        'address': '',
        'judge': judge,
        'hearing_date': '',
        'hearing_time': '',
    }