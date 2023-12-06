def userRecords(users):
    print("User Records")
    print(users)
    print(type(users))


#userRecords(["ram","shyam","hari"])
#userRecords(("ram","shyam","hari"))
#userRecords(users=["ram","shyam","hari"])

# *args 


def employeeRecords(*args):
    print("Employee Records")
    print(args)
    print(type(args))


employeeRecords("ajay","shyam","hari")    
    
# if args is not the last parameter
# if args is last parameter then pass keyword argument
#def employeeRecords2(x,*emps):
def employeeRecords2(*emps,x):
    print("x = ",x)
    print("Employee Records")
    print(emps)
    print(type(emps))
        

employeeRecords2("ajay","shyam","hari",x=100)        