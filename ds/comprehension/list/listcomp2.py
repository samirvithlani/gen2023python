students =[100,20,33,45,67,89,98]
studentseven =[i for i in students if i%2 ==0]

# for i in students:
#     if i %2 ==0:
#         studentseven.append(i)

print(studentseven)        

users = ["amit","jay","raj","parth","amita","neha","jaya","rekha","amitabh","anil","akshit","ami","an"]
filusers =[i.upper() for i in users if i.startswith("a") and len(i)>3]
print(filusers)

# filusers =[]
# for i in users:
#     if i.startswith("a") and len(i)>3:
#         filusers.append(i.upper())
        
# print(filusers)
        