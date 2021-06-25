from contact_manager.contact import Contact
from contact_manager.mail_sender import MailSender


class EmailableContact(Contact, MailSender):
    pass
