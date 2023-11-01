data = [[1,2,3],[4,5,6],[7,8,9]]
#[[0[0],0[1],0[2]],[1[0],1[1],1[2]],[2[0],2[1],2[2]]]
sum =0
sumlist =[]

for i in range(0,len(data)):
    sum=0
    for j in range(0,len(data[i])):  
        sum = sum + data[i][j]
        print(data[i][j],end=" ")
        
    print(sum,end=" ")    
    sumlist.append(sum) #list 
        
    
    print()    

print(sumlist)    

#a shop keepr has 7 days sales data of 2 times morning data and evening data
#find total weekly sales data
# find heightest sales data..
# which day has heightest sales data