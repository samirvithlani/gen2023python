x = lambda name : max(name.split(),key=len)

ans = x("hi this is xms india")
print(ans)


def findMax(a,b):
    if a>b:
        return True
    
    return False    

x1 = lambda a,b : findMax(a,b)

ans1 = x1(10,20)
print(ans1)


def convert(name):
    
    if name == name[::-1]:
        return name.upper()
    else:
        return name.title()



x2 = lambda name : convert(name)
print(x2("malayalam"))   
print(x2("malayalama")) 
    
    
#name --> palindrom --> uuper case... title case...
