studentNameRoll={
    "A":"subrata",
    "B":"Ausama",
    "C":"Vikash",
    "D":"Aashi",
    "E":"Gaurav",
    "E":"Edward"
}

print(studentNameRoll["A"]) # subrata

studentNameRoll["A"]="Munoor"

print(studentNameRoll["A"]) # Munoor

del studentNameRoll["A"]

print("**** After delete **** ")

print(studentNameRoll)