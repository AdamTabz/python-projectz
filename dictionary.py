dictionary={"netherlands":"Amsterdam","france":"Paris","china":"Bejing"}
print(dictionary["china"])
dictionary["canada"]="Toronto"
print(dictionary["canada"])
del dictionary ["netherlands"]
print(dictionary)
for key,value in dictionary.items():
    print(key, value)
