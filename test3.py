import logging
import math


class BaseCalculator(object):
    def __init__(self, angle, number1, number2):
        self.angle = angle
        self.number1 = number1
        self.number2 = number2

    def multiplication_of_two_numbers(self):
        """This Function Multiplies the 2 Numbers
        and returns the Value
        """
        return self.number1 * self.number2

    def division_of_two_numbers(self):
        """This Function Divides the 2 Numbers
        and returns the Value
        """
        return self.number1 / self.number2

    def subtraction_of_two_numbers(self):
        """This Function 2 returns the Diffrence
        between Two Numbers
        """
        return self.number1 - self.number2

    def addition_of_two_numbers(self):
        """This Function Adds the 2 Numbers
        and returns the Value
        """
        return self.number1 + self.number2


class ScientificCalculator(BaseCalculator):
    def __init__(self, angle, number1, number2):
        BaseCalculator.__init__(self, angle, number1, number2)

    def sine(self):
        """This Function returns the sine of the Angle"""
        return math.sin(self.angle)

    def cosine(self):
        """This Function returns the Cosine of the Angle"""
        return math.cos(self.angle)

    def tangent(self):
        """This Function returns the Tangent of the Angle"""
        return math.sin(self.angle) / math.cos(self.angle)


def getAngle(types):
    while True:
        try:
            angle = int(input("Enter the Angle in Degrees:"))  # Gets the Angle

        except ValueError:
            logging.error(
                "You Entered invalid Input. Try Again with Valid Input"
            )
            continue

        if angle > 180:
            logging.error("You Cannot Give Angle Greater than 180")
            continue

        if angle <= 180:
            break

    return angle, 0, 0  # returns angle alone & with number1,number2  as 0


def getNumbers(types):
    while True:
        try:
            number1 = int(
                input("Enter the First Number:")
            )  # Gets First Number
            number2 = int(
                input("Enter the Second Number:")
            )  # Gets Second Number

        except ValueError:
            logging.error(
                "You Entered invalid Input. Try Again with Valid Input"
            )
            continue

        if types != 4:
            break

        elif types == 4:
            try:
                number1 / number2
                return 0, number1, number2
                break

            except ZeroDivisionError:  # Exception had been Handled
                logging.error("You Cannot divide By Zero")
                logging.error("Please Try Again")
                continue

    return 0, number1, number2  # returns number1,number2 alone & angle as 0


def main():
    while True:
        try:
            print()
            print("What need to be done ?")
            print("\n1.Addtion")
            print("\n2.Subtraction")
            print("\n3.Multiplication")
            print("\n4.Division")
            print("\n5.Sine")
            print("\n6.Cosine")
            print("\n7.Tangent")
            print("\n8.Exit\n")
            types = int(input("Select any one from above:"))

        except ValueError:
            logging.error(
                "You Entered invalid Input. Try Again with Valid Input"
            )
            continue

        if types == 1 or types == 2 or types == 3 or types == 4:
            print()
            angle, number1, number2 = getNumbers(types)
            objects = ScientificCalculator(
                angle, number1, number2
            )  # Creating the Object
            print()
            if types == 1:
                print(
                    "Adding {} & {} gives {}".format(
                        number1, number2, objects.addition_of_two_numbers()
                    )
                )
                continue

            elif types == 2:
                print(
                    "Subtracting {} & {} gives {}".format(
                        number1, number2, objects.subtraction_of_two_numbers()
                    )
                )
                continue

            elif types == 3:
                print(
                    "Multiplying {} & {} gives {}".format(
                        number1,
                        number2,
                        objects.multiplication_of_two_numbers(),
                    )
                )
                continue

            elif types == 4:
                print(
                    "Dividing {} & {} gives {}".format(
                        number1,
                        number2,
                        round(objects.division_of_two_numbers(), 2),
                    )
                )
                continue

        elif types == 5 or types == 6 or types == 7:
            print()
            angle, number1, number2 = getAngle(types)
            objects = ScientificCalculator(
                angle, number1, number2
            )  # Creating the Object
            print()
            if types == 5:
                print("Sin {}' is {}".format(angle, objects.sine()))
                continue
            elif types == 6:
                print("Cos {}' is {}".format(angle, objects.cosine()))
                continue
            elif types == 7:
                print("Tan {}' is {}".format(angle, objects.tangent()))
                continue

        elif types == 8:
            print("\nExiting...........")
            print("\nExited")
            break

        elif types > 8:
            logging.error(
                "You Selected Invalid Choice. Try Again with Valid Choice"
            )


if __name__ == "__main__":
    main()

# Complexity
# O(1) or O(n)

# For Test Coverage
# coverage run -m test3
# coverage report -m
# coverage html
