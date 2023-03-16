import unittest
import requests

# API_URL = 'http://127.0.0.1:5000'
API_URL = 'http://172.23.0.2:5000'

class TestScientificCalculator(unittest.TestCase):

    def test_calculate_square_root(self):
        number = 25
        expected_result = 5.0
        response = requests.post(f"{API_URL}/sqrt", json={"number": number})
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], expected_result)

    def test_calculate_factorial(self):
        number = 5
        expected_result = 120
        response = requests.post(f"{API_URL}/factorial", json={"number": number})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], expected_result)

    def test_calculate_ln(self):
        number = 2.71828182846
        expected_result = 1.0
        response = requests.post(f"{API_URL}/ln", json={"number": number})
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], expected_result)

    def test_calculate_power(self):
        number = 2
        power = 3
        expected_result = 8
        response = requests.post(f"{API_URL}/power", json={"number": number, "power": power})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], expected_result)

if __name__ == '__main__':
    unittest.main()
