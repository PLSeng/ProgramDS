class Rat(object):

    def __init__(self, num, den):
        self._num = num
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        else:
            self._den = den

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        self._num = num

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        else:
            self._den = den

    def simplify(self):
        # Function to simplify the rational number
        gcd = self.find_GCD(self.num, self.den)
        return Rat(self.num // gcd, self.den // gcd)

    def find_GCD(self, a, b):
        # Function to find the greatest common divisor
        while b:
            a, b = b, a % b
        return a

    def printDetail(self):
        print(f"{self.num}/{self.den}")
