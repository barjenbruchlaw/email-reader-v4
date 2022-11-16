import logging
from script_addnewcase import getEmails as getEmails_addnewcase
from script_receivednewcase import getEmails as getEmails_receivednewcase

logging.basicConfig(filename='email_log.log', encoding='utf-8', level=logging.DEBUG)

logging.info('Received new case')

receivednewcase_digest = getEmails_receivednewcase()

for email_dict in receivednewcase_digest:
    logging.info(email_dict)

logging.info('Add new case')

addnewcase_digest = getEmails_addnewcase()

for email_dict in addnewcase_digest:
    logging.info(email_dict)







