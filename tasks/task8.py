name = "java"

# ind = name.index("a")
# print(ind)

ind = -1

for i in range(len(name)):
    if name[i] =="a":
        ind = i
        break

print(ind)        
