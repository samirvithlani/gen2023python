# def myfun():
#     pass

#lambda : anonymous function , lambda  keyword
# lambda params : expression
#withput return type and without args
demo = lambda : print("Hello World")
demo()

#lambda a[args / param ] : expression / body
demo2 = lambda a : print("value of a = ",a)
demo2(100) #100 /a


demo3 = lambda a ,b, c : print("value of a = ",a,"value of b = ",b,"value of c = ",c)
demo3(100,200,300)



demo4 = lambda name : print("Hello ",name.upper())
demo4("sachin")

