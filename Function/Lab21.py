
# Defination of the Function
def getAdd(*value):
    sum=0
    for a in value:
        sum=sum+a
    return sum


print("-------------")
sum1=getAdd(10,20,30,40)
print(sum1)
print("-------------")
sum2=getAdd(10)
print(sum2)
print("-------------")
sum3=getAdd(10,20)
print(sum3)
print("-------------")
sum4=getAdd(10,40)
print(sum4)
print("-------------")
