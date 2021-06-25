from contact_manager.contact_list import ContactList


class Contact:
    all_contacts: ContactList = ContactList()

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
