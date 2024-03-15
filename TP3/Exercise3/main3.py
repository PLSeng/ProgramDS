from Calculation import Calculation
from Rat import Rat


class main3:

    a = Rat(2, 3)
    b = Rat(3, 6)

    cal1 = Calculation.add(a, b)

    cal1.printDetail()

    cal1 = Calculation.subtract(a, b)

    cal1.printDetail()

    cal1 = Calculation.multiply(a, b)

    cal1.printDetail()

    cal1 = Calculation.divide(a, b)

    cal1.printDetail()

    c = Rat(1,0)

    c.printDetail()