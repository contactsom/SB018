class Employee:
    "This is Employee Class"
    employeeName="Subham"
    employeeAge=26
    employeeCompany="Simplilearn"

    def __init__(self,employeeSalery,employeeDesignation):
        self.employeeSalery=employeeSalery
        self.employeeDesignation = employeeDesignation

    def sayHi(self):
        print(self.employeeName)
        print(self.employeeAge)
        print(self.employeeCompany)
        print(self.employeeSalery)
        print(self.employeeDesignation)

# Creating the Object
# Here Employee() is a constructor of the Employee Class
# Whereas  employee is a object of the Employee Class
employee=Employee(5000,"AVP")
employee.sayHi()
