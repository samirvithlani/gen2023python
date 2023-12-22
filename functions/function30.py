#["","","",""]

#filter,map,reduce
#fitlter will return the values which are true --> 2 param -->
#map will return all the values : --> 4 param -->
#reduce will return only one value : -> 1

#what is predicate statement --> true or false -->

#filter

users = ["amit","parth","ram","shyam","sita","geeta","hr","p"]
#users1= [i for i in users if len(i)>3]

# users1 = list(filter(lambda x: len(x) > 3,users))
# print(users1)


users1 = list(filter(lambda x : x.startswith("s"),users))
print(users1)

# for i in users:
#     if len(i)>3:
#         users1.append(i)
