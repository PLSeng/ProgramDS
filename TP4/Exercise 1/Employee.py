class Employee:

    def __init__(self, name, emp_id, exp):
        self._name = name
        self._id = emp_id
        self._exp = exp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, emp_id):
        self._id = emp_id

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, exp):
        self._exp = exp

    def display_info(self, endLine="\n"):
        print(f"Name: {self._name}, ID: {self._id}, Experience: {self._exp}", end=endLine)
