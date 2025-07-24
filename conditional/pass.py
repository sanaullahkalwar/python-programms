# per = int(input("Enter percentage: "))
# if per >= 33:
#     print("Pass")
# else:
#     print("Fail")
    
    
studentsNames = []
studentsMarks = []
studenstResult= []
for i in range(5):
    names = input(f"Enter Name {i+1} : ")
    studentsNames.append(names)
    marks = int(input(f"Enter Your marks {i+1} : "))
    studentsMarks.append(marks)
    if studentsMarks[i]>50:
        studenstResult.append("Pass")
    else:
        studenstResult.append("Fail")


print(studentsNames)
print(studentsMarks)        
print(studenstResult)