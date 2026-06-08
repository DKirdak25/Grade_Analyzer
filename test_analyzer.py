"""
                Tests
this file contain all type of test which are needed for this project

"""
import unittest
from unittest.mock import patch
from logic import Analyzer
from interface import get_student

class TestAnalyzer(unittest.TestCase):
				"""  Tests for Analyzer """
				
				def setUp(self):
								"""
								Create Analyzer and set of markd for use in all test methode
								"""
								marks = [30, 90]
								self.my_analyzer = Analyzer(marks)
								
				def test_average(self):
								""" Test that check return average properly """
								my_result = self.my_analyzer.average()
								
								self.assertEqual(60, my_result)
				
				def test_lowest(self):
								""" Test that check return lowest properly """
								my_result = self.my_analyzer.lowest()
								self.assertEqual(30, my_result)
				
				def test_highest(self):
								"""Test that check return highest properly """
								my_result = self.my_analyzer.highest()
								self.assertEqual(90, my_result)
								
				def test_passed(self):
								""" Test that check return passsed student numbers properly """
								my_result = self.my_analyzer.passed_students()
								self.assertEqual(1, my_result)
				
				def test_invalid_type(self):
								""" Test that check not accept invalid type"""
								with self.assertRaises(TypeError):
												Analyzer("hello")
								
				
				def test_empty_list(self):
								""" Test that check empty list """
								with self.assertRaises(ValueError):
												Analyzer([])


class TestInterface(unittest.TestCase):
				# Tests for User Interface 
				
				def test_get_student(self):
								""" Test that check get student function """
								with patch("builtins.input", side_effect=["30", "q"]):
												result = get_student()
								
								self.assertEqual([30], result)
				
				def test_empty_then_valid(self):
								""" Test that check invalid input """
								with patch("builtins.input", side_effect=["", "101", "-5", "abc", "50", "q"]):
												result = get_student()
												
								self.assertEqual([50], result)
								
								

if __name__=="__main__":
				unittest.main()		