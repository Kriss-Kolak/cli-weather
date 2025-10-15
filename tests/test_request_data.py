import unittest
from functions.request_data import get__current_temperature

class GetCurrentTemperatureTests(unittest.TestCase):

    def test_basic_type_case(self):
        result = get__current_temperature(50, 50)
        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], str)
    
    def test_invalid_latitude(self):
        with self.assertRaises(Exception):
            result = get__current_temperature(91,50)
    
        
    def test_invalid_longitude(self):
        with self.assertRaises(Exception):
            result = get__current_temperature(50,91)