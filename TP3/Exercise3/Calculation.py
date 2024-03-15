from Rat import Rat

class Calculation:

    @staticmethod
    def add(rat1, rat2):
        # Function to add two rational numbers
        den = rat1.den * rat2.den
        num = (rat1.num * rat2.den) + (rat2.num * rat1.den)
        return Rat(num, den).simplify()

    @staticmethod
    def subtract(rat1, rat2):
        # Function to subtract two rational numbers
        den = rat1.den * rat2.den
        num = (rat1.num * rat2.den) - (rat2.num * rat1.den)
        return Rat(num, den).simplify()

    @staticmethod
    def multiply(rat1, rat2):
        # Function to multiply two rational numbers
        num = rat1.num * rat2.num
        den = rat1.den * rat2.den
        return Rat(num, den).simplify()

    @staticmethod
    def divide(rat1, rat2):
        # Function to divide two rational numbers
        num = rat1.num * rat2.den
        den = rat1.den * rat2.num
        return Rat(num, den).simplify()