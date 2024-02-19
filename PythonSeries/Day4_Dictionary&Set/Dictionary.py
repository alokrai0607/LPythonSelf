StudentInfo = {
    "StName" : "Alok",
    "Subject":["Java","Python","JavaScript","CSS","HTML"],
    "coNo":('9044414580','7880667919','7007304517'),
    "age" : 29,
    "marks":95.5,
    "Male":True
}



print(StudentInfo)  # {'StName': 'Alok',
                    #'Subject': ['Java', 'Python', 'JavaScript', 'CSS', 'HTML'], 
                    #'coNo': ('9044414580', '7880667919', '7007304517'), 
                    #'age': 29, 'marks': 95.5, 'Male': True}

print(type(StudentInfo))  #<class 'dict'>

#Print by indexes

print(StudentInfo["StName"])  #Alok
print(StudentInfo["Subject"])  # ['Java', 'Python', 'JavaScript', 'CSS', 'HTML']
print(StudentInfo["coNo"]) #('9044414580', '7880667919', '7007304517')
print(StudentInfo["age"]) #29
print(StudentInfo["marks"]) #95.5
print(StudentInfo["Male"])  #True

print(StudentInfo)


nullDic = {}
print(nullDic)  #{}







