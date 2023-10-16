# data = {}
# print(data)
# print(type(data))

data = {101:"amit",1002:"raj",78:"rajesh",33:"amit"}

print(data)

data[1002]="RAJ KUMAR"
data[1003]="PARTH"

data.update({10:"janvi",11:"kajal",101:"amit kumar"})


keyData = data.keys()
print("keys ",keyData)

valueData = data.values()
print("values ",valueData)


for k,v in data.items():
    print(k," -- ",v)