class Calculator:
    """Do addition, subtraction, multiplication and division."""

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

class SuperCalculator(Calculator):
    """Do addition, subtraction, multiplication, division, square and cube."""

    def addition(self, num1, num2, num3):
        return num1 + num2 + num3

    def square(self, num1):
        return num1 * num1

    def cube(self, num1):
        return num1 * num1 * num1

my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47, 12)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)