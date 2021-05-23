"""Module to practice unittesting with python"""
import unittest

import main


class TestMain(unittest.TestCase):
    """temp"""

    def test_do_stuff(self):
        """Test the do stuff method with an integer"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """Test the do stuff method with a string"""
        test_param = "jhuhaud"
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)


unittest.main()
