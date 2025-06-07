class Employee:
    def __init__(self,name):
        self.name=name
        print("I am Constructor")
        print(self.name)


# Creating the Object
# Here Employee() is a default constructor of the Employee Class
# Whereas  employee is a object of the Employee Class
#employee1=Employee()

# Here Employee() is a Argument constructor of the Employee Class
employee2=Employee("Gouttam")

#employee3=Employee()
