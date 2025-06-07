# Global Decleration
tax=50 # Global Variable

# Defination of the Function
def state1():
    tax=20 # Local Variable
    print(tax)

def state2():
    tax = 70 # Local Variable
    print(tax)

def state3():
    print(tax)

def state4():
    global tax
    tax=33
    print(tax)

def state5():
    print(tax)

def state6():
    print(tax)

# Caller
state1()
state2()
state3()
state4()
state5()
state6()