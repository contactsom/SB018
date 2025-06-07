class ParenClass:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} says Hello")


class ChildClass(ParenClass):
    def __init__(self,name,age):
        super().__init__(name)
        #self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Hi, I am {self.age} Years Old!!")

child=ChildClass("Sourav",22)
child.speak()