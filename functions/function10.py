def findMax(users):  #user list...
    return max(users)



x = findMax([10,20,30,22,34,8])
print("max ",x)



def getSqare(nos):
    
    nos1 = []
    
    for i in nos:
        nos1.append(i*i)

    return nos1     


x = getSqare([1,2,3,4,5])
print(x)   


def getSquare1(nos):
    
    return [i*i for i in nos]


x = getSquare1([1,2,3,4,5])
print(x)

    