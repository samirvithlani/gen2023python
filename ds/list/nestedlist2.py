users = [[1,2],[4,5],[7,8],[77,99],[87,90,67]]
print(users)

''''
    int a[3][3]
    
    for(i=0;i<3;i++){
        
        for(j=0;j<3;j++){
            print(a[i][j])
        }
    }


'''
#users = [[1,2,11],[4,5,33],[7,8,44]]
#5
print(len(users))
#0
for i in range(0,len(users)):
    
    print("len...",len(users[i]))
    
    for j in range(0,len(users[i])):
        print(users[i][j], end=" ")
    
    print()    
        


# for i in users:
#     #print(i)
#     for j in i:
#         print(j, end=" ")
    
#     print()    


# for i,j in users:
#     print(i,"-",j)