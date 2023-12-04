def isAlive(flag):
    
    if flag == 0:
        return True
    
    return False


ans =  isAlive(1)
print(ans)

if isAlive(10):
    print("Alive")
else:
    print("Not Alive")    