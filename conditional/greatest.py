#this program will take 3 inputs and tell which one is greater then other two
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater then {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater theen {num1} and {num3}")
else:
    print(f"{num3} is greater then {num1} and {num2}")


