num = int(input("Enter any number: "))

if (num%3==0 and num%5==0):
    print(f"{num} is multiple  both 3 and 5")
elif (num%3==0):
    print(f"{num} is multiple of 3")
elif (num%5==0):
    print(f"{num} is multiple of 5")
else:
    print("Number is not multiple of both")