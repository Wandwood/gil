from django.test import TestCase, Client
# Create your tests here.

class ResponseTestCase(TestCase):
    def test_logging(self):
        c = Client()
        response1 = c.post('/create/', {'username': 'Zhenya', 'password': '112233'})
        print(response1.status_code)
        self.assertEqual(response1.status_code, 200)
        
    