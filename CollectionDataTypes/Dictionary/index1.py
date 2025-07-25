#this program will create the dictionary in python
students_Info = {
    "name": "sanaullah",
    "age": 27,
    "Education": "Master's"
}

#accessing the dictionary
print(students_Info["name"])

#other way to access the element of dictionary
print(students_Info.get("age"))


#adding a value to dictionary
students_Info["Email"]= "sanullahkalwar@gmail.com"
print(students_Info.get("Email"))

#updating and existing value in the dictionary
students_Info["age"]=28
print(students_Info.get("age"))


#Removing and Deleting items from the dictionary
print("-----------------------")
print(students_Info)
print("------------------")

students_Info.pop("age")
print(students_Info)

del students_Info["Email"]
print(students_Info)

#clear out the complete dictionary
students_Info.clear()
print(students_Info)