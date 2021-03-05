import unittest
from unittest1 import ScientificCalculator

class UnitTest1Test(unittest.TestCase):
	def test_division_of_two_numbers(self):
		self.assertEqual(int(ScientificCalculator(120,1,1).division_of_two_numbers),1);

if __name__ == '__main__':
    unittest.main()