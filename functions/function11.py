def printData(*args):
    print(args)
    return [i**2 if i %2 ==0 else i ** 3 for i in args]


x = printData(1,2,3,4,5)
print(x)

def checkPalindrom(name):
    
    return name  == name[::-1]

x = checkPalindrom("madam")
print("x -->",x)

if checkPalindrom("malayalam"):
    print("palindrom")
else:
    print("not palindrom")    

