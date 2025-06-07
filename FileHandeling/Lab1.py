file = open("simple.txt",'w')
print("File Name : ",file.name)
print("File Mode : ",file.mode)

print("File Redable : ",file.readable()) # False
print("File Write : ",file.writable()) # True

print("File Closed ? : ",file.closed) #  False
file.close()

print("File Closed ? : ",file.closed) # True