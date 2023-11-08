data ={"mon":[12,22],"tue":[13,12],"wed":[12,7],"thu":[2,2],"fri":[22,10],"sat":[15,18],"sun":[30,0]}

print(data)
k = data.keys() #list
print(k)
v = data.values() #list
print(v)

i = data.items() #list(tuple)
print(i)



# for i in data.items():#[(),(),(),(),(),(),()]
#     for j in i:
#         print(j)


# for k,v in data.items():
#     print(k)
#     print(v)

#data ={"mon":[12,22],"tue":[13,12],"wed":[12,7],"thu":[2,2],"fri":[22,10],"sat":[15,18],"sun":[30,0]}

print("monday",data["mon"])
data["mon"]=[22,22]
print(data)

data["jan"]=[100,100]

print(data)

data.update({"feb":[200,200],"jan":[100,110]})
print(data)