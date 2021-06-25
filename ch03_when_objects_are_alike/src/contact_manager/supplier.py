from contact_manager.contact import Contact


class Supplier(Contact):
    def order(self, order):
        print(f"If this were a real system we would send '{order}' order to '{self.name}'")
