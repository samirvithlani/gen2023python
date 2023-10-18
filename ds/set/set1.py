#[]
#()
#{} --> dict
#{}

#users =set({}) #empty set
users = set({100,20,45,456,78,90,78,67,45})
#print(type(users))
print(users)

l = len(users)
print("set",l)


users.add(109)

#users.remove(202)
#users.discard(202)


#users.update([77,88,99,100])
#users.update({77,88,99,100})
#users.update((77,88,99,100))
#users.update("hello python")

x = users.pop()
print("removing...",x)



for i in users:
    print(i)
 