"""
User Authentication Testing
"""
import unittest
import json
from appApi import app

class AppApiTestCase(unittest.TestCase):
    """ Authenication """
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"vic", 
                     "email":"vic@gmail.com",
                     "password":"longpassword"
                    }
    def test_login(self):
        """ login API Testing """
        self.app = app.test_client()
        response = self.app.post('/auth/v1/login', data={"username":"keynote", "password":"pass123"
                                                        })
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """ signup API Testing """
        response = self.app.post('/auth/v1/signup', data=json.dumps(self.data), 
                                 content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["username"], "vic")
        self.assertEqual(result["email"], "vic@gmail.com")
        self.assertEqual(result["password"], "longpassword")
        self.assertEqual(response.status_code, 201)   
if __name__ == '__main__':
    unittest.main()
