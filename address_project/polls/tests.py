from django.test import TestCase

import unittest
from django.test import Client
from polls.models import StateJapan, Company


class TestAddress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        StateJapan.objects.create(state_name="Karnataka", state_desc="Southern state")
        StateJapan.objects.create(state_name="Telangana", state_desc="Divided telugu state")
        Company.objects.create(company_name="Company11",
                               building_number="393",
                               postal_code="560-102",
                               locality="HSR",
                               city="Bangalore",
                               state=StateJapan.objects.get(state_name="Karnataka"))
        Company.objects.create(company_name="Company22",
                               building_number="393",
                               postal_code="560-102",
                               locality="HSR",
                               city="Bangalore",
                               state=StateJapan.objects.get(state_name="Karnataka"))

    def test_pincode(self):
        """
        Tests pincode api
        :return: Passed or Failed
        """
        client = Client()
        response = client.get('/polls/pincode/1')
        self.assertEqual(response.status_code, 200)  # url test
        self.assertEqual(response.data, [{"postal_code": "560-102"}])  # pincode min 1 test

        response = client.get('/polls/pincode/-1')  # negative number test
        self.assertEqual(response.status_code, 404)

        response = client.get('/polls/pincode/abc')  # string failure test
        self.assertEqual(response.status_code, 404)

    def test_company(self):
        """
        Tests company api
        :return: Passed or Failed
        """
        client = Client()
        response = client.get('/polls/company/')
        self.assertEqual(response.status_code, 200)
