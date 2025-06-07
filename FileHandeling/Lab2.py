file = open("simple.txt",'r')
print("File Name : ",file.name)
print("File Mode : ",file.mode)

print("File Redable : ",file.readable()) # True
print("File Write : ",file.writable()) # False

print("File Closed ? : ",file.closed) #  False
file.close()

print("File Closed ? : ",file.closed) # True