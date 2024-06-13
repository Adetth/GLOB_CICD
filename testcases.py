import unittest
from app import app
import json

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.post('/add', data=json.dumps({'num1': 10, 'num2': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 15)

    def test_subtract(self):
        response = self.app.post('/subtract', data=json.dumps({'num1': 10, 'num2': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 5)

    def test_multiply(self):
        response = self.app.post('/multiply', data=json.dumps({'num1': 10, 'num2': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 50)

    def test_divide(self):
        response = self.app.post('/divide', data=json.dumps({'num1': 10, 'num2': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 2.0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
