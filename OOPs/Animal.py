class Animal:
    def eat(self):
        print("Animal can eat")

    def sleep(self):
        print("Animal can Sleep")


class Dog(Animal):
    def bark(self):
        print("Dog can Bark")


dog1=Dog()
dog1.bark()
dog1.eat()
dog1.sleep()


