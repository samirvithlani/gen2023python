def getUserData():
    name = "ram"
    age = 99
    
    nameFlag = True
    ageFlag = True
    
    if age < 18:
        ageFlag = False
    
    for i in name:
        if " " in i:
            nameFlag = False
    
    if nameFlag and ageFlag:
        return "valid"    
    else:
        return "invalid"        
    
            
        
    
        

x = getUserData()
print(x)            
   