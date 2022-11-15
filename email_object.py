class EmailObject:
    def __init__(self, email_dict):
        self.email_dict = email_dict
        self.message_id = email_dict['message_id']
        self.datetime = email_dict['datetime']
        self.sender = email_dict['sender']
        self.county = email_dict['county']
        self.ef_number = email_dict['ef_number']
        self.plaintiff_name = email_dict['plaintiff_name']
        self.resident_1_name = email_dict['resident_1_name']
        self.address = email_dict['address']
        self.case_number = email_dict['case_number']
        self.judge = email_dict['judge']
        self.hearing_date = email_dict['hearing_date']
        self.hearing_time = email_dict['hearing_time']