#users = []  #emplty list
users = ["ram","shyam","neha","sita","gita"]

print(users)
print(type(users))
# print(users[0])
# print(users[1])
# print(users[2])
# print(users[3])
# print(users[4])

#List is mutable --> we can modify the list
users[0]="ram kumar"
print(users)
l = len(users)
print(l)



# for i in range(0,l):
#     print(users[i])

for i in users:
    print(i)