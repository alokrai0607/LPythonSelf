#Nested dictionary
Student = {
    "name" : "Alok",
    "score": {
        "chem": 95,
        "math": 90,
        "phy": 92   
    }
}

print(Student) #{'name': 'Alok', 'score': {'chem': 95, 'math': 90, 'phy': 92}}


print(Student["score"]) #{'chem': 95, 'math': 90, 'phy': 92}


#if we want to return all keys present in dictionary
print(Student.keys())  #dict_keys(['name', 'score'])


#if we want to return all values then
print(Student.values())  #dict_values(['Alok', {'chem': 95, 'math': 90, 'phy': 92}])


#return all key value pairs as tupple
print(Student.items()) #dict_items([('name', 'Alok'), ('score', {'chem': 95, 'math': 90, 'phy': 92})])



