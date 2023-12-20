#decorators with arguments


def isManager(func): #func =getData
    def inner(manager): #manager =yes
        print("manager is",manager)
        if manager == "yes":
            func()
        else:
            print("Not eligible")    
            
    return inner


@isManager
def getData():
    print("Eligible to get data")

getData("yes")    
    