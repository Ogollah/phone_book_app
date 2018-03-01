""" importing library for unit test"""
import unittest
from contact import Contacts

class TestContactsCase(unittest.TestCase):

    # test create contact
    def test_create_contact(self):
        contact = Contacts()
        response = contact.create_contact("manu", "0712345678")
        self.assertEqual(response['message'], 'Contact created!')


    def test_delete_contact(self):
        contact = Contacts()
        response = contact.delet_contact(contact)
        self.assertEqual(response['message'], 'Contact deleted!')

if __name__ == '__main__':
       unittest.main()