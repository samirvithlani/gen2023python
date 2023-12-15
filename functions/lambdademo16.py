demo1 = lambda *args: args # (10,20,30)
x = demo1(10,20,30)
print(x)


demo2 = lambda *args : list(args)
x1 = demo2(10,20,30)
print(x1)


demo3 = lambda *args : max(args)
x2 = demo3(10,20,30)
print(x2)

#sum()

demo4 = lambda *args : sum(args)
x3 = demo4(10,20,30)
print(x3)


#can we iterate lambda function

demo5 = lambda *args : [i**2 for i in args]
x4 = demo5(10,20,30)
print(x4)
