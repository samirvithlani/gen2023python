#MAP   --> same length array as input
#Filter : -> it might be smaller than input
#reduce :- > it will be single value

#map demo 1


data = [1,2,3,4,5,6,7,8,9,10]

# x = list(map(lambda x: x ** 2,data))
# print(x)

x = list(map(lambda x: x**2 if x %2 ==0 else x**3,data))
print(x)

# x = [i**2 for i in data]
# print(x)


users = ["amit","ram","shyam","mike","jane","tom","tim","peter","john","jennie"]


x = list(map(lambda x: x.upper(),users))
print(x)
# x = [i.upper() for i in users]
# print(x)

