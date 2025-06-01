studentNameRoll={
    "A":"subrata",
    "B":"Ausama",
    "C":"Vikash",
    "D":"Aashi",
    "E":"Gaurav",
    "X":"XXXXX"
}

#print(studentNameRoll["E"])
studentNameRoll.setdefault("X","Default Value")
print(studentNameRoll["X"]) #
print(studentNameRoll)