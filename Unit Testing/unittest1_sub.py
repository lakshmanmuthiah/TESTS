import unittest
from unittest1 import ScientificCalculator

class UnitTest1Test(unittest.TestCase):
	def test_subtraction_of_two_numbers(self):
		self.assertEqual(ScientificCalculator(120,1,1).subtraction_of_two_numbers,0);

if __name__ == '__main__':
    unittest.main()