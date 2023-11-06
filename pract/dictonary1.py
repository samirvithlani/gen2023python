#key value --> dictionary
'''
    dict is mutable
    dict is unordered
    dict is not indexed
    dict does not allow duplicate keys
    dict allows duplicate values
    dict stores data in key value pair
    dict allows heterogenous data[key, value..]
    {} --> dict
    [] --> list
    () --> tuple
    
    data type pf dict is dict
'''

#users = {} # empty dict
users = {1:"raj",2:"ram",3:"amit",4:"raj",2:"RAM"}

print(type(users))
print(users)
#x is list of tuples
x = users.items()
print(x)

# for i in x:
#     for j in i:
#         print(j,end=" ")
#     print()    

for i,j in users.items():
    print(i,j)