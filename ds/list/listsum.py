pers = [10,20,3,40,5,60,7,22]
sum = 0

for i in pers:
    #sum = sum + i
    sum+=i

print(sum)    


age =[[10,20],[20,30],[30,40]]

agesum =[]

sum1=0
for i in age:
    for j in i:
        sum1+=j
    print(sum1,end="  ")
    agesum.append(sum1)
    sum1=0    
    
    print()            
    


#find max element from list...    

#pers = [10,20,3,40,5,60,7,22]
max1 = pers[0] # max = 10

for i in pers:
    #10 > 10 FALSE
    # 20 > 10 TRUE
    # 3 > 20 FALSE
    # 40 > 20 TRUE
    # 5 > 40 FALSE
    # 60 > 40 TRUE
    # 7 > 60 FALSE
    # 22 > 60 FALSE
    if i >max1:
        max1 = i # max = 20, max = 40 max = 60
        


print("max = ",max1)       

#age =[[10,20],[20,30],[30,40]] 

#print("max = ",max(agesum))
print("age sum array..",agesum)

print("max = ",max(agesum))