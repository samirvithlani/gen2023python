#decorators....

#1. function inside a function
#2. function as a parameter to another function
#3. function returning another function

#func is not kwyword, it is a variable
def order_food(func): #100 [","] #throw_party #3
    
    def inner(): #5
        print("I want to order food") #6
        #func =100 ,
        func() #throw_party() #7
    
    return inner #4


@order_food #2 
def throw_party():
    print("Throwing a party") #8


throw_party() #1