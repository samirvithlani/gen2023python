name = "ahmedbad"

# x = name.index("a")
# print("index of a = ",x)

x = -1
for i in range(0,len(name)):
    if name[i]=="a":
        x = i
        

print("index of a = ",x)  



def findIndex(name,ch):
    
    for i in range(0,len(name)):
        if name[i]==ch:
            return i
    return -1

ind = findIndex(name,"k")
print("index of m = ",ind)


def findLastIndex(name,ch):
    
    in1 = -1
    for i in range(0,len(name)):
        if name[i]==ch:
            in1 = i
    
    return in1
  
  
inddex = findLastIndex(name,"q") 
print("index of a = ",inddex)