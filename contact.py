""" This class handles adding,viewing, updating, and deleting of contacts"""

class Contacts(object):
    
    def __init__(self):
        self.contact_list = [] #create contact list
    
    def create_contact(self, name, phon_num):
        """ creating contacts in a dictionary"""
        contact = {}
        contact['name'] = name
        contact['phon_num'] = phon_num
        self.contact_list.append(contact) #append contacts to contact list
        return {"message": "Contact created!"}

    #view contact
    def view_contact(self, contact):
        for contact in self.contact_list:
            return contact

        #delete function
    def delete_contact(self, contact):
        if contact in self.contact_list:
            self.contact_list.remove(contact)
        return {'message':'Contact deleted!'}

    #update function
    def update_contact(self,contact):
        for contact in self.contact_list:
            if contact == contact:
                contact['']
        return {'message': 'Contact updated!'}