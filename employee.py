class Employee:
    def __init__(self):
        self.EmployeeName = ""
        self.EmployeeId = ""
        self.EmployeeDept = ""
        self.EmployeeSalary = 0

    def getEmployeeDetails(self):
        """Very Important (DUM) Function to get the details of the employee"""
        self.EmployeeName = input("Enter Employee Name: ")
        self.EmployeeId = input("Enter Employee Id: ")
        self.EmployeeDept = input("Enter Employee Dept: ")
        self.EmployeeSalary = input("Enter Employee Salary: ")

    def showEmployeeDetails(self):
        """Another not ver important(DUM) funciton to display the details of employee"""
        print("-Employee Details-")
        print(f"Employee Name: {self.EmployeeName}")
        print(f"Employee ID: {self.EmployeeId}")
        print(f"Employee Department: {self.EmployeeDept}")
        print(f"Employee Salary: {self.EmployeeSalary}")

    def updateEmployeeSalary(self):
        self.EmployeeSalary = input(
            f"Enter updated Salary for the employee {self.EmployeeName}: ")


Foo = Employee()
Foo.getEmployeeDetails()
Foo.showEmployeeDetails()
Foo.updateEmployeeSalary()
Foo.showEmployeeDetails()

