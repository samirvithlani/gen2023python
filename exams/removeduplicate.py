data = [10,20,30,10,20,10,40,60,70,10,55]
res =[]


for i in data:
    if i not in res:
        res.append(i)

print(res)        

# res1 =[]
# res1 = [i for i in data if i not in res1]
# print(res1)
