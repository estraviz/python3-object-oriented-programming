from contact_manager.address_holder import AddressHolder
from contact_manager.contact import Contact


class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
