from appApi import app
import unittest
import json

class AppApiTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.client = app.test_client()
        self.data = {
        "id": 1,
        "name":"Ugali",
        "price": 30
    }

    def test_get_meal_options(self):
        response = self.client.post('/v1/meals', data = self.data)
        self.assertEqual(response.status_code,201)
       

    def test_add_meal_option(self):
        response = self.client.post('/v1/meal', data={'id':6,'name':'pitza', 'price':90})
        self.assertEqual(response.status_code, 201)
        


    def test_update_meal_info(self):
        response = self.client.post('v1/meal', data={'id':7, 'name':'mbuta', 'price':5})
        self.assertEqual(response.status_code,201)
        response = self.client.put('/v1/meal/7', data={"id":7, 'name':'mbuta', 'price':10})
        self.assertEqual(response.status_code, 201)

    def test_delete_meal(self):
        response = self.client.post('v1/meal', data={'id':2, 'name':'maziwa', 'price':25})
        self.assertEqual(response.status_code,201)
        response = self.app.delete('/v1/meal/2', data={"id":2, "name":"maziwa", "price":25})
        self.assertEquals(response.status_code,201)

    
    def test_get_menu(self):
        self.app = app.test_client()
        response = self.app.get('/v1/menu')
        self.assertEquals(response.status_code,200)

    def test_update_meal_choice(self):
        response = self.client.post('v1/meal', data={'id':2, 'name':'maziwa', 'price':25})
        self.assertEqual(response.status_code,201)
        response = self.app.put('/v1/meal/2',data={"id":2, "name":"Sembe", "price":20})
        self.assertEquals(response.status_code,200)

    def test_specific_order(self):
        response = self.client.post('v1/meal', data={'id':11, 'name':'guarana', 'price':250})
        self.assertEqual(response.status_code,201)
        response_in_Json = json.loads(response.data.decode('utf-8').replace("'", "\""))
        result = self.client.get('v1/meal/{}'.format(response_in_Json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('guarana', str(result.data))

    
    def test_get_all_meals(self):
        self.app = app.test_client()
        response = self.app.get('/v1/meals')
        self.assertEquals(response.status_code,200)


    def tearDown(self):
        
        pass


if __name__ == '__main__':

	unittest.main()
