import json
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse 

class PeopleTestCase(APITestCase):
    
    def test(self):
        response = self.client.get('/people/', {'pk': 1})
        self.assertEqual(response.status_code, 200)

class CompanyTestCase(APITestCase):
    
    def test(self):
        
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 200)

