myset1={1,2,3,4,5,6,7,8}
print(myset1)

myset2={"A","B","C","D"}
print(myset2)

print("***** After Update ****")

unionset=myset1.union(myset2) # merge in to myset1 not myset2
print(myset1)
print(myset2)
print(unionset)
