# -5, -4, -3, -2, -1 -> -Ve Index
# 10, 20, 30, 40, 50
# 0,  1,  2,  3,  4  -> +Ve Index


a=(10,20,30,40,50)
print("Before Change ")
print(a[0]) # 10

a[0]=100

print("After Change ")
print(a[0]) # TypeError: