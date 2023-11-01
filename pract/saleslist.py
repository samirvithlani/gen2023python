sales = [[100,200],[200,300],[300,400],[400,500],[500,600],[600,700],[700,800]]

weeklysales = 0
daylist = []
sum =0

for i in range(0,len(sales)):
    sum =0
    for j in range(0,len(sales[i])):
        weeklysales = weeklysales + sales[i][j]
        sum = sum + sales[i][j]
    daylist.append(sum)
    


print(max(daylist))
print(weeklysales)        
print(daylist)