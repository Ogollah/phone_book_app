""" importing library for unit test"""
import unittest
from contact import Contacts

class TestContactsCase(unittest.TestCase):
    
    # test create contact
    def test_create_contact(self):
        contact = Contacts()
        response = contact.create_contact("manu", "0712345678")
        self.assertEqual(response['message'], 'Contact created!')

        # test view contact
    def test_view_contact(self):
        contact = Contacts()
        response = contact.create_contact("manu", "0712345678")
        response = contact.view_contact(contact)
        self.assertEqual(response, {'name':"manu", 'phon_num':"0712345678"})

    def test_delete_contact(self):
        contact = Contacts()
        response = contact.delete_contact(contact)
        self.assertEqual(response['message'], 'Contact deleted!')

    #test update contact
    def test_update_contact(self):
        contact = Contacts()
        response = contact.update_contact(contact)
        self.assertEqual(response['message'], 'Contact updated!')
 


    
if __name__ == '__main__':
       unittest.main()
