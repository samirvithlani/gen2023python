

try:
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    ans = no1 / no2
    print("Division is: ", ans)
except ZeroDivisionError:
    print("Cannot divide by zero")  
except ValueError:
    print("Please enter only numbers")      

print("End of program")