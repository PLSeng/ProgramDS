from tabulate import tabulate


class Employee:

    def __init__(self):
        self.employee = {}

    def addEmployee(self, empID: str, empName: str, empSalary: float, empDepartment: str) -> None:
        self.employee[empID] = {
            'empName': empName,
            'empSalary': empSalary,
            'empDepartment': empDepartment
        }

    def printEmpDetail(self, empID: str) -> str:
        emp = self.employee
        if empID in emp:
            print('-' * 30)
            print(
                f"Employee name: {emp[empID]['empName']}, \nEmployee salary: {emp[empID]['empSalary']}, \nEmployee Department: {emp[empID]['empDepartment']}")
            print('-' * 30)
        else:
            print('Employee not found!')

    def updateEmp(self, empID: str, empName=None, empSalary=None, empDepartment=None) -> None:
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

            print(f"Update successful. Changed information are: ", end='')
            for i in range(len(_change_Controller) - 1):
                print(_change_Controller[i], end=', ')
            print(_change_Controller[-1] + '.')
        else:
            print('No Employee Found!')

    def calculateEmpSalary(self, empID: str, workingHours: int) -> str:
        if empID in self.employee:
            OT = ((workingHours - 50) * (self.employee[empID]['empSalary'] / 50)) if workingHours - 50 > 0 else 0
            salary = self.employee[empID]['empSalary'] + OT
            return f"{'-' * 30}\nEmployee ID: {empID}\nEmployee Name: {self.employee[empID]['empName']}\nSalary: {salary}\n{'-' * 30}"
        else:
            return 'No Employee Found!'

    def printAllEmployee(self) -> None:
        employee_list = []
        for emp_id, emp_data in self.employee.items():
            employee_list.append([emp_id, emp_data['empName'], emp_data['empSalary'], emp_data['empDepartment']])

        print(tabulate(tabular_data=employee_list, headers=['ID', 'Name', 'Salary', 'Department'], tablefmt='fancy_grid'))
