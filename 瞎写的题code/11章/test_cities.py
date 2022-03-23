#11-2 11-3
import unittest
from city_functions import city_function

class CityFunctionTest(unittest.TestCase):
    """test the city function"""

    def test_city_country(self):
        """能否正确处理 Santiago Chile吗"""
        city_country = city_function("santiago","chile")
        self.assertEqual(city_country,"Santiago, Chile")

    def test_city_country_population(self):
        """能否正确处理包含人口的城市和国家"""
        city_country_population = city_function("santiago","chile",5000000)
        self.assertEqual(city_country_population,"Santiago, Chile -population 5\
000000")

unittest.main()
