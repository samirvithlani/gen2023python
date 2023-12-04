#function naming convention: userDetail()
#without args and without return type

def test():
    print("This is test function")
    print("this function is without args and without return type")


test() #calling function

#without return type with args
def userDetail(name,age):
    print("Name is ",name)
    print("Age is ",age)
    print("This function is with args and without return type")


userName = input("Enter name: ")
userAge = int(input("Enter age: "))

#userDetail("Ram",20) #calling function")

#call by value
userDetail(userName,userAge) #calling function    
    