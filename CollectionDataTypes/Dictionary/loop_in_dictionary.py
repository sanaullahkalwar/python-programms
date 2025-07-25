students_Info = {
    "name": "sanaullah",
    "Email": "sanullahkalwar@gmail.com",
    "Age": 27
}

#method 1
for key in students_Info:
    print(key, " - ", students_Info[key])
    
#second method
for key, value in students_Info.items():
    print(f"{key} - {value}")
    
    
#Some methods of dictionary
print(students_Info.keys())
print(students_Info.values())
print(students_Info.items())

