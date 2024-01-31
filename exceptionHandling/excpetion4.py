
age = int(input("Enter your age: "))

try:
    if age<18:
        raise ValueError("Age cannot be less than 18")
except ValueError as e:
    print(e)    

    