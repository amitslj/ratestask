import unittest
from src.main import get_custom_rates
import pandas as pd


class TestRates(unittest.TestCase):
    """
    This class will be called to run the test cases for rates application
    """

    def test_custom_prices(self):
        """
        description:
            This method runs 2 test cases to fetch custom prices :
            1. Asserts if the converted Dataframe is not None
            2. Asserts if the data contains 10 rows corresponding to each date
        """
        price = get_custom_rates('CNSGH', 'north_europe_main', '2016-01-01', '2016-01-10')
        df = pd.DataFrame(price)

        self.assertIsNotNone(df)
        self.assertEqual(df.shape[0], 10)

    def test_null_prices(self):
        """
        description:
            This method runs 2 test cases to validate Null prices :
            1. Asserts if the price returned is Null for 2016-01-13
            2. Asserts if the data contains 1 rows corresponding the date queried
        """
        price = get_custom_rates('CNSGH', 'north_europe_main', '2016-01-03', '2016-01-03')
        df = pd.DataFrame(price)

        self.assertIsNone(df['price'].values[0])
        self.assertEqual(df.shape[0], 1)


if __name__ == '__main__':
    unittest.main()
