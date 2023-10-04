data = input("enter string: ")
c = input("enter character: ")
ind = -1
#java
#a

# for i in range(len(data)):
#     #  data[0] == a j ==a #false
#     # data[1] == a a ==a #true
#      if data[i]==c:
#         ind = i #ind = i , i =1 , ind =1
#         break

# print("index = ",ind)    


print(len(data))
#java  --> 4
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4]) #error..

#len(data) 4 -1 = 3
for i in range(len(data)-1,-1,-1):
    
    if data[i]==c:
        ind = i
        break

print("index = ",ind)        
