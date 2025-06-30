#this program will check if a number is multiple of 3 and 5.
num=int(input("Enter any positive number: "))
if num%3==0 and num%5==0:
    print(f"Yes!!! {num} is multiple of 3 and 5..")
elif num%3==0 and num%5!=0:
    print(f"{num} is only  multiple of 3")
elif num%3!=0 and num%5==0:
    print(f"{num} is only multiple of 5")
else:
    print(f"No!!! {num} is not multiple of 3 and 5")