myset1={1,2,3,4,5,6,7,8}
myset2={1,2,3,4,50,60,70,80}

myset1.update(myset2)
newUnionSet=myset1.union(myset2)

print("Update",myset1)
print("Union",newUnionSet)