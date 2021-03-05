import math
import unittest

class BaseCalculator(unittest.TestCase):
    def __init__(self, angle, number1, number2):
        self.angle = angle
        self.number1 = number1
        self.number2 = number2
    
    @property
    def multiplication_of_two_numbers(self):
        """This Function Multiplies the 2 Numbers
        and returns the Value
        """
        return self.number1 * self.number2
    
    @property
    def division_of_two_numbers(self):
        """This Function Divides the 2 Numbers
        and returns the Value
        """
        return self.number1 / self.number2
    
    @property
    def subtraction_of_two_numbers(self):
        """This Function 2 returns the Diffrence
        between Two Numbers
        """
        return self.number1 - self.number2
    
    @property
    def addition_of_two_numbers(self):
        """This Function Adds the 2 Numbers
        and returns the Value
        """
        return self.number1 + self.number2


class ScientificCalculator(BaseCalculator):
    def sine(self):
        """This Function returns the sine of the Angle"""
        return math.sin(self.angle)

    def cosine(self):
        """This Function returns the Cosine of the Angle"""
        return math.cos(self.angle)

    def tangent(self):
        """This Function returns the Tangent of the Angle"""
        return math.tan(self.angle)