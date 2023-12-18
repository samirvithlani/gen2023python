def outer(a,b):
    print("outer function")
    
    def inner(no1,no2):
        print("inner function")
        return no1+no2
    
    return inner(a,b)
    


pow = outer(10,2)   
print("pow is",pow)