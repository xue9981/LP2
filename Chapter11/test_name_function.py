import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """can this program process name like 
        Janis Joplin correctly?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """can this program process name like
        Wolfgang Amadeus Mozart?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

        
