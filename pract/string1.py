#string is immutable --> same reference we can not modify
#char a[10] =>string a="hello" --> size dynamically allocated
#string stores data in indexing.... 0 1 2 3 4 5 6 7 8 9

name = "Good Morning"
print(name)
print(type(name))

#'\0' null character

l = len(name)
print(l)

# for i in range(0,len(name)):
#     print(name[i])

for i in name:
    print(i)



#A 65 a 97 space 32
# print(name[0])
# print(name[1])
# print(name[2])
