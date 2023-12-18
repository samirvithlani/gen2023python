#nested functions

# def outer():
#     print("outer function")
    
#     def inner():
#         print("inner function")
    
#     inner()


# outer()        

def outer(a):
    print("outer function",a)
    
    def inner(no):
        print("inner function",no)
        print("outer param to inner ",a)
    
    
    #print("outer function param of inner",no) error
    inner(20)


outer(30)   


    