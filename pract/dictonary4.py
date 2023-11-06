sales = {"mon": 100, "tue": 200, "wed": 300, "thu": 400, "fri": 500, "sat": 600, "sun": 700}
#sales ={1:1000,2:2000,3:3000,4:4000,5:5000,6:6000,7:7000}
print(sales)

#removedvalue = sales.pop(2) #you have to pass key to remove it
removedvalue = sales.pop("thu") #you have to pass key to remove it
print("removing...",removedvalue)


remvkvpair = sales.popitem() #no argument should be passed it will remove last item and return it
print("removing...",remvkvpair)

print(sales)