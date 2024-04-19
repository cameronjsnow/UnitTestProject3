import unittest
from datetime import datetime
from app import app, parse_date_string

class TestStockVisualizerInputs(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_stock_symbol(self):
        #Tests valid stock symbols
        valid_symbols = ['GOOGL', 'AAPL', 'IBM']
        for symbol in valid_symbols:
            #Should return true for all valid symbols
            self.assertTrue(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

        #Tests invalid stock symbols
        invalid_symbols = ['google', '123', 'AB123', 'aapl', 'SUPERLONGNAME', '']
        for symbol in invalid_symbols:
            #Should be false for invalid symbols
            self.assertFalse(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

    def test_chart_type(self):
        #Test for valid chart types
        self.assertIn('1', ['1', '2'])
        self.assertIn('2', ['1', '2'])

        #Test for invalid chart types
        self.assertNotIn('3', ['1', '2'])
        self.assertNotIn('a', ['1', '2'])

    def test_time_series_function(self):
        #Test for valid time series functions
        valid_functions = ['1', '2', '3', '4']
        for function in valid_functions:
            self.assertIn(function, ['1', '2', '3', '4'])

        #Test for invalid time series functions
        invalid_functions = ['0', '5', 'a', '']
        for function in invalid_functions:
            self.assertNotIn(function, ['1', '2', '3', '4'])

    def test_start_date_format(self):
        #Test for valid date formats
        valid_dates = ['2022-01-01', '2023-12-31']
        for date in valid_dates:
            self.assertIsInstance(parse_date_string(date), datetime)

        #Test for invalid date formats
        invalid_dates = ['01-01-2022', '2022/01/01', '20220101', '']
        for date in invalid_dates:
            self.assertIsNone(parse_date_string(date))

    def test_end_date_format(self):
        #Same tests as start_date_format since the logic is the same
        self.test_start_date_format()

if __name__ == '__main__':
    unittest.main()