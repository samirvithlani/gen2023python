emails = [" a@gmail.com ","ram@ gmail.com ","amit@gmail.com","  k@gmail .com"]

def checkEmail(x):
    space = False
    x = x.strip()
    print("xxx",x)
    for i in x:
        if " "  in i:
            space = True
            break
    
    return space    
            
            
    
    

newlist = list(filter(lambda x: checkEmail(x),emails))
print(newlist)