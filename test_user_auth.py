from appApi import app
import unittest
import json

class AppApiTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "username":"vic", 
            "email":"vic@gmail.com",
            "password":"longpassword"
            }
       

    def test_login(self):
       self.app = app.test_client()
       response = self.app.post('/auth/v1/login',data={"username":"keynote","password":"pass123"})
       self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.app.post('/auth/v1/signup', data = json.dumps(self.data) , content_type = 'application/json')
        response = self.app.post('/auth/v1/signup',data={"username":"keynote","password":"longpassword", "email":"vic@gmail.com"})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

    

if __name__ == '__main__':
    unittest.main()
