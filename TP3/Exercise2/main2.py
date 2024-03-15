from Employee import Employee


class main2:
    employee = Employee()

    employee.addEmployee('E01', 'PLSeng', 5000.00, 'AMS')

    employee.printEmpDetail('E01')

    employee.updateEmp('E01', empSalary=6000.00)
    employee.updateEmp('E01', empName='PAV Limseng', empSalary=5500.00)
    employee.printEmpDetail('E01')
    employee.addEmployee('E02', 'HSLong', 10000, 'GIC')
    employee.printEmpDetail('E02')

    employee.updateEmp('E02', empDepartment='AMS')
    employee.printEmpDetail('E02')

    print(employee.calculateEmpSalary('E01', 72))
    print(employee.calculateEmpSalary('E02', 40))
