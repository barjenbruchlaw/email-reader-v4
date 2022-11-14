class EmailObject_MO:
    def __init__(self, email_dict):
        self.email_dict = email_dict
        self.datetime = email_dict['datetime']
        self.sender = email_dict['sender']
        self.ef_number = email_dict['ef_number']
        self.plaintiff_name = email_dict['plaintiff_name']
        self.resident_1_name = email_dict['resident_1_name']
        self.address = email_dict['address']