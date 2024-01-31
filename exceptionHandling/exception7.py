from MyException import InValidAgeException

age = int(input("Enter your age: "))

try:
    if age<18:
        raise InValidAgeException("Age cannot be less than 18")
except InValidAgeException as e:
    print(e)    
