#anno

# def printData():
#     print("Hello World")

# printData = lambda:print("Hello World")
# printData()


# def printData(name):
#     print(name)
# data = lambda name:print(name)
# data("Hello World")

# data = lambda a,b : print(a+b)
# data(10,20)


# data  = lambda a,b : a+b
# ans = data(100,20)
# print(ans)


# data = lambda a,b :a if a >b else b
# maxelm = data(100,20)
# print(maxelm)



# data = lambda a,b,c : a if a >b and a>c else b if b>c else c
# maxelm = data(100,20,300)
# print(maxelm)


def checkName(name):
    flag = False
    
    if name == name[::-1]:
        flag = True
    
    return flag



x = lambda name: True if checkName(name)  else False    
ans = x("madam")
print(ans)




