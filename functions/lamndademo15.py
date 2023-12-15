# def myFun(x):
#     return x


demo = lambda x : x +100

ans = demo(100)
print(ans)


demo2 = lambda fname, lname : fname + " "+lname

fullname = demo2("sachin","yadav")
print(fullname) 



circle = lambda r: 3.14 * (r*r)
circlearea = circle(10)
print(circlearea)

#no argument and return type


p = lambda : 10 * 10
p1 = p()
print(p1)
    
    