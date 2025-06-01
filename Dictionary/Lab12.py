studentNameRoll={
    "A":"subrata",
    "B":"Ausama",
    "C":"Vikash",
    "D":"Aashi",
    "E":"Gaurav",
    "E":"Edward"
}

print("**** Before delete **** ")
print(studentNameRoll)

del studentNameRoll["A"]
del studentNameRoll["B"]
del studentNameRoll["C"]
del studentNameRoll["D"]
del studentNameRoll["E"]

print("**** After delete **** ")

print(studentNameRoll) # {}