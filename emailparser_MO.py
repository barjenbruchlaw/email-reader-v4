import base64

def emailparser(datetime, sender, subject, payload):

    data = payload['parts'][0]['parts'][0]['parts'][0]['body']['data']
    data = data.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    decoded_data_string = str(decoded_data)

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