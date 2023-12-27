def getData(*args):
    return list(map(lambda x: x**2, args))


x  = getData(1,2,3,4,5,6,7,8,9,10)
print(x)


def getName(name):
    return list(map(lambda x: x.upper(), name))

y = getName("raj")
print(y)


data = []

data.extend("samir")
print(data)


a = [1,2,3]
b = [4,5,6]

ans = list(map(lambda x,y:x+y,a,b))
print(ans)


fname = ["amit","raj","parth"]
lname = ["patel","shah","patel"]

fullname = list(map(lambda x,y: x +" "+ y,fname,lname))
print(fullname)




