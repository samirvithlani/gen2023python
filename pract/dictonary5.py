sales = {"mon": 100, "tue": 200, "wed": 300, "thu": 400, "fri": 500, "sat": 600, "sun": 700}

sum = 0
for k,v in sales.items():
    sum = sum + v
    
print("Total sales: ",sum)    


#only get values from dict

val = sales.values() #it will return list of values
print(val)

sum1 = 0
for i in val:
    sum1 = sum1 + i

print("Total sales: ",sum1)    


k = sales.keys() #it will return list of keys
print(k)