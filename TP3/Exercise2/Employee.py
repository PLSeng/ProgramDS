class Employee:

    def __init__(self):
        self.employee = {}

    def addEmployee(self, empID, empName, empSalary, empDepartment):
        self.employee[empID] = {
            'empName': empName,
            'empSalary': empSalary,
            'empDepartment': empDepartment
        }

    def printEmpDetail(self, empID):
        emp = self.employee
        if empID in emp:
            print('-' * 30)
            print(
                f"Employee name: {emp[empID]['empName']}, \nEmployee salary: {emp[empID]['empSalary']}, \nEmployee Department: {emp[empID]['empDepartment']}")
            print('-' * 30)
        else:
            print('Employee not found!')

    def updateEmp(self, empID, empName=None, empSalary=None, empDepartment=None):
        emp = self.employee
        _change_Controller = []
        if empID in emp:
            if empName is not None:
                emp[empID]['empName'] = empName
                _change_Controller.append('Employee Name')
            if empSalary is not None:
                emp[empID]['empSalary'] = empSalary
                _change_Controller.append('Employee Salary')
            if empDepartment is not None:
                emp[empID]['empDepartment'] = empDepartment
                _change_Controller.append('Employee Department')

            print(f"Update successful. Changed infomation are: ", end='')
            for i in range(len(_change_Controller) - 1):
                print(_change_Controller[i], end=', ')
            print(_change_Controller[-1] + '.')
        else:
            print('No Employee Found!')

    def calculateEmpSalary(self, empID, workingHours):
        if empID in self.employee:
            OT = ((workingHours - 50) * (self.employee[empID]['empSalary'] / 50)) if workingHours - 50 > 0 else 0
            salary = self.employee[empID]['empSalary'] + OT
            return f"{'-' * 30}\nEmployee ID: {empID}\nEmployee Name: {self.employee[empID]['empName']}\nSalary: {salary}\n{'-' * 30}"
        else:
            return 'No Employee Found!'
