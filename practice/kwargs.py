def getStudentData(marks,name,age,city):
    print(name,age)
    print(marks)
    print(city)


#getStudentData("John",20)    
#getStudentData(20,"john")    
getStudentData(100,age=20,name="john",city  = "mumbai")



#*name = *args

def employeesName(data,*names,x):
    print(names)
    print(type(names))
    print(x)
    print(data)


employeesName("amit","ram","shyam",x="mohan")    





