import unittest
from unittest1 import ScientificCalculator

class UnitTest1Test(unittest.TestCase):
	def test_multiplication_of_two_numbers(self):
		self.assertEqual(ScientificCalculator(120,1,1).multiplication_of_two_numbers,1);

if __name__ == '__main__':
    unittest.main()