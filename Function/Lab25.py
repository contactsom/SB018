# Global Decleration
tax=50 # Global Variable

# Defination of the Function
def state1():
    tax=20 # Local Variable
    print(tax)

def state2():
    tax = 70 # Local Variable
    print("I am Global :: ",globals()['tax'])
    print("I am Local :: ",tax)

def state3():
    print(tax)


# Caller
state1()
state2()
state3()
