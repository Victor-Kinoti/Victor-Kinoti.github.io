""" Menu functionalty"""
import unittest
import json
from appApi import app


class AppApiTestCase(unittest.TestCase):
    """Main class for Testing """
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.client = app.test_client()
        self.data = {"id": 1,
                     "name":"Ugali",
                     "price": 30
                    }

    def test_get_meal_options(self):
        """tests getting a single meal option"""
        self.data = {"id": 4,
                     "name":"ngwashe",
                     "price": 50
                    }
        response = self.client.get('/v1/meals/4', data=json.dumps(self.data), 
                                   content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["id"], 4)
        self.assertEqual(result["name"], "ngwashe")
        self.assertEqual(result["price"], 50)
        self.assertEqual(response.status_code, 201)
       

    def test_add_meal_option(self):
        """tests adding a single meal to the option"""
        response = self.client.post('/v1/meal', data=json.dumps(self.data))
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "Ugali")
        self.assertEqual(result["price"], 30)
        self.assertEqual(response.status_code, 201)
        


    def test_update_meal_info(self):
        """tests updating  meal"""
        response = self.client.put('/v1/meal/1', data=json.dumps(self.data))
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["price"], 30)
        self.assertEqual(result["name"], "Ugali")
        self.assertEqual(response.status_code, 201)

    def test_delete_meal(self):
        """tests deleting a meal from option"""
        response = self.client.post('v1/meal', data=json.dumps(self.data))
        self.assertEqual(response.status_code, 201)
        del_response = self.app.delete('/v1/meal/2', data=json.dumps(self.data), 
                                       content_type='application/json')
        self.assertEqual(del_response.status_code, 200)
    def test_get_menu(self):
        """tests getting the menu"""
        self.app = app.test_client()
        response = self.app.get('/v1/menu', data=json.dumps(self.data), 
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)  
    def test_get_all_meals(self):
        """tests getting all meals"""
        self.app = app.test_client()
        response = self.app.get('/v1/menu', data=json.dumps(self.data),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
