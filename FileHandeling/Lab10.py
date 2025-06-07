file = open("Simplilearn.txt",'r') # Read
data=file.readlines()

for line in data:
    print(line)


file.close()

