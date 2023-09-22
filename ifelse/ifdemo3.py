salary = int(input("Enter your salary: monthly* "))
yearly_salary = salary * 12

if yearly_salary>=200000 and yearly_salary<500000:
    print("you are eligible for 2 wheeler loan")

elif yearly_salary>=500000 and yearly_salary<1000000:
    print("you are eligible for 2 wheeler loan")
    print("you are eligible for 3 wheeler loan")
    print("you are eligible for 4 wheeler loan")

elif yearly_salary>=1000000:
    print("you are eligible for 2 wheeler loan")
    print("you are eligible for 3 wheeler loan")
    print("you are eligible for 4 wheeler loan")
    print("you are eligible for Home loan")

else:
    print("raise your salary !!!")    
        