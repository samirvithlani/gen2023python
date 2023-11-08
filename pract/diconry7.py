data ={"mon":[12,22],"tue":[13,12],"wed":[12,7],"thu":[2,2],"fri":[22,10],"sat":[15,18],"sun":[30,0]}

# m = data["mon"]
# print(m)
# msum =0
# for i in m:
#     msum = msum + i
#     print(i)

# print(msum)    
daywisesum =[]
daywisesumdict ={}

sum=0
weeksum =0
for k,v in data.items():
    sum =0
    for i in v:
        print(i,end=" ")
        sum = sum + i
        weeksum = weeksum + i
    daywisesum.append(sum)
    daywisesumdict.update({k:sum})
    print()    

print(daywisesum)
print(daywisesumdict)
print("weekkly sum = `",weeksum)