data = [i for i in range(1,10)]
print(data)

matrix = [[j for j in range(1,4)] for i in range(1,4)]
print(matrix)


data =[["a","b","c"],["d","e","f"],["g","h","i"]]

#using list comprehension convert above data into uppercase


data3=[]
for i in range(0,3):
    for j in range(0,3):
        data3.append(data[i][j].upper())     
print(data3)        
        


data1 = [[j.upper() for j in i] for i in data]
print(data1)