class ContactList(list):

    def search(self, string):
        solution = []
        for i in self:
            if string in i.name:
                solution.append(i)
        return solution

    def longest_name(self):
        s = {i.name: len(i.name) for i in self}
        try:
            mylist = sorted(s)[0]
            return mylist
        except:
            return None


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts.clear()


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        new = {self.email: string}
        Supplier.all_orders.update(new)
        print (Supplier.all_orders)
