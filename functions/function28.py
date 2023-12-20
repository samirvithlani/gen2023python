def isallInt(func):
    
    def inner(numbers):#numbers = [10,20,30]
        for i in numbers:
            #print(type(i))
            if type(i)!=int:
                print("Please enter valid numbers")
                break
                
        
        return func(numbers) #getMarks([10,20,30])    
    
    return inner


@isallInt
def getMarks(numbers):
    print("Marks are",numbers)
    

getMarks([10,20,30,"ok"]) #inner                