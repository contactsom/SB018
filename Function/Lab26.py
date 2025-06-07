a=100

def m1():
    a=10
    def m2():
        a=1
        print("I am in m2 :: ",a)
    m2()
    print("I am in m1",a)

m1()