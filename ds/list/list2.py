users = ["raj","ram","ram","parth","sita","gita"]

print(users)

# users.append("mohan")
# users.extend(["rohan","sohan","mohan"])


cnt = users.count("ram")
print("cnt = ", cnt)


if cnt>0:
    users.remove("ram")
else:
    print("rama not found")    

#removedeml = users.pop()
#removedeml = users.pop(2)
#users.remove("ram")
#print("removedeml = ", removedeml)


for i in users:
    print("i = ", i)