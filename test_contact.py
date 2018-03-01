""" importing library for unit test"""
import unittest
from contact import Contacts

class TestContactsCase(unittest.TestCase):

    # test create contact
    def test_create_contact(self):
        contact = Contacts()
        response = contact.create_contact("manu", "0712345678")
        self.assertEqual(response['message'], 'Contact created!')



if __name__ == '__main__':
       unittest.main()