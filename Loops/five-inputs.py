#in this program we will take five inputs and store them in the list
mylist=[]
for i in range(5):
    num = input(f"Enter any numbers {i+1}: ")
    mylist.append(num)
    
print(mylist)