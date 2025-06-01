myset={1,2,3,4,5,6,7,8}
length= len(myset)
i=0
while(i<length):
    print(myset[i]) # TypeError: 'set' object is not subscriptable
    i=i+1
