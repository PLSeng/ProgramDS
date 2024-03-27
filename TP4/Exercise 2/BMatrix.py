from tabulate import tabulate

class BMatrix(object):
    def __init__(self, data: list[list[float]]):
        self.data_ = data
        self.nl_ = len(data)  # Number of lines (rows)
        self.nc_ = len(data[0]) if data else 0  # Number of columns, checks if data is not empty

    @property
    def nl(self):
        return self.nl_

    @property
    def nc(self):
        return self.nc_

    def same_size(self, other: 'BMatrix') -> bool:
        return self.nl == other.nl and self.nc == other.nc

    def element_at(self, l: int, c: int) -> float:
        # Ensure the requested indices are within the matrix bounds
        if l < 0 or l >= self.nl_ or c < 0 or c >= self.nc_:
            raise IndexError("Row or column index out of bounds")
        return self.data_[l][c]

    def set_element_at(self, l: int, c: int, value: float):
        # Ensure the requested indices are within the matrix bounds
        if l < 0 or l >= self.nl_ or c < 0 or c >= self.nc_:
            raise IndexError("Row or column index out of bounds")
        self.data_[l][c] = value

    def __str__(self):
        return tabulate(self.data_, tablefmt="fancy_grid")

    def show(self):
        print(self)
