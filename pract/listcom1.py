users = [1,2,3,4,5,6,7]
userssq =[i**2 for i in users]

# for i in users:
#     userssq.append(i**2)

# print(userssq)    


#string list...
users = ["java","python","c","c++","ruby","perl"]
useruper =[i.upper() for i in users]

# for i in users:
#     useruper.append(i.upper())

print(useruper)    

data = [1,2,3,4,5,6,7,8,9,10]
fildata = [i**2 if i%2 ==0 else i**3 for i in data]

# for i in data:
#     if i %2 ==0:
#         fildata.append(i**2)
#     else:
#         fildata.append(i**3)

print(fildata)           


data1 = ["java","python","c","cpp","ruby","perl","hr"]
fildata1 =[i.upper() if len(i)>3 else i.title() for i in data1]

# for i in data1:
#     if len(i)>3:
#         fildata1.append(i.upper())
#     else:
#         fildata1.append(i.title())    

print(fildata1)        

 


