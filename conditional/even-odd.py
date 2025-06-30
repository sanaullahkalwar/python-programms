#this program will check if the number is even or odd
number = int(input("Enter the number: "))
print(f"You entered this number: {number}")

if number>0:
    if number%2==0:
        print("Given number is even...")
    else:
        print("Given number is odd...")
else:
    print("Please enter positive number")