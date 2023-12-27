
def checkParams(func):
    
    def inner(a,b):
        if type(a)!= int or type(b)!=int:
            print("Invalid parameters")
        else:
            func(a,b)    
    
    return inner        

@checkParams
def add(a,b):
    print(a+b)


add(10,"20")    