def getUserData(users):
    print(users)
    for i in users:
        print(i)



#getUserData("java")    
getUserData(["java","python","c++"])
# getUserData(("java","python","c++"))
# getUserData({"java","python","c++"})


def getEmployeeData(emps):
    empList = []
    for i in emps:
        empList.append(i.upper())
    return empList


x = getEmployeeData(["java","python","c++"])
print("x = ",x)