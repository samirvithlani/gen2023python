def smartDiv(func):
    
    def inner(a,b): #a=10,b=2
        if b ==0:
            print("Please enter valid number")
        else:
            return func(a,b) #div(10,2)
        
    return inner

@smartDiv
def div(a,b): #a=10,b=2
    print(a/b)


div(10,0) #inner             
    