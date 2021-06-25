from typing import List

from contact_manager.contact import Contact


class ContactList(list):
    def search(self, name):
        matching_contacts: List[Contact] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
