from DataAnalyst import DataAnalyst
from DataScientist import DataScientist


class Main1:
    if __name__ == "__main__":
        john_doe = DataScientist("John Doe", 'DS001', '3 years', "Machine Learning", ["Python", "R"])
        jane_smith = DataAnalyst("Jane Smith", 'DA001', '5 years', ["Excel", 'sql'], 10)

        john_doe.display_info()
        jane_smith.display_info()
