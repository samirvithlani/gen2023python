def isManager(func): #getData
    def inner(emp):
        if emp == 'manager':
            print('I am a manager')
            func()#getData()
        
    return inner    


@isManager
def getData():
    print("I am a employee")


getData("manager1")    