from city_functions import city_countries
import unittest

class CityTestCase(unittest.TestCase):
    """test for city_countries"""
    def test_city_country(self):
        testname = city_countries("santiago", "chile")
        self.assertEqual(testname, "Santiago, Chile")

    def test_population(self):
        testname = city_countries("santiago", "chile", 50000000)
        self.assertEqual(testname, "Santiago, Chile - population" \
                         + " 50000000")

unittest.main()
