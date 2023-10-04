# data =[] #empty list

# print("data = ", data)
# print("type(data) = ", type(data))

#index...
data = [10,30,40,12,2]

print("data = ", data)
l = len(data)
print("len = ", l)

# for i in range(0,l):
#     print("data[",i,"] = ", data[i])
    


#data.extend([1,2,3,4,5])
data.append(78)
data.append(90)
data.append(89)
data.append(33)
data.append(44)

data.extend([99,77,123,987])


data.insert(2,1001)



for i in data:
    print("i = ", i)  