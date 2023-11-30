data = set({"python","java","c","c++","python","java"})

removedElm = data.pop()
print("removed element",removedElm)


while len(data)>0:
    x =data.pop()
    print("removed element",x)

print(data)    