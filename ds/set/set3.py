a = set({"amit","raj","jay"})
b = set({"amit","raj","sumit"})

x = a.union(b)
print(x)

x = a.intersection(b)
print(x)

x = a.difference(b)
print("diff...",x)

x = a.symmetric_difference(b)
print(x)


#a.difference_update(b)
#a.symmetric_difference_update(b)
#print(a)

a = set({"amit","raj","jay","sumit"})
b = set({"amit","raj","sumit","jay","x"})


#flag = a.issubset(b)
flag = a.issuperset(b)
print(flag)
