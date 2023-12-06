#**kwargs

#kwargs should be last parameter in function
def userData(x,y,**kwargs):
    print("x = ",x)
    print(kwargs)
    print(type(kwargs))
    


userData(100,200,name="amit", age=30, city="pune",)    