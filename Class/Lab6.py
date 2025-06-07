## Both Constructor should not be there at the same time
class Employee:

    def __init__(self,name):
            self.name=name
            print("I am argument Constructor")
            print(self.name)

'''
def __init__(self):
        print("I am default Constructor")
'''

# Creating the Object
# Here Employee() is a default constructor of the Employee Class
# Whereas  employee is a object of the Employee Class
employee1=Employee()

# Here Employee() is a Argument constructor of the Employee Class
employee2=Employee("Gouttam")

employee3=Employee()
