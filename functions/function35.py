
from functools import reduce

#reduce... map filter hIgher order functions
marks = [10,20,30,40,50]
#using reduce function
# 10 + 20 = 30
#a = 30 + 30 = 60
#a = 60 + 40 = 100
#a = 100 + 50 = 150

x = reduce(lambda a,b: a + b, marks)
print(x)

add = ["201","surbhi","complex","ahmedbad"]

address = reduce(lambda a,b: a + "," + b, add)
print(address)

#find max from list using reduce...
data = [10,101,20,34,55,4,32]

maxElm = reduce(lambda a,b: a if a > b else b, data)
print(maxElm)