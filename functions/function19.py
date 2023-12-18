def outer(a,b):
    print("outer function")
    
    def inner(no1,no2):
        print("inner function")
        return no1+no2
    
    ans = inner(10,20)
    print("ans is",ans)
    
    return a **b


pow = outer(10,2)   
print("pow is",pow)