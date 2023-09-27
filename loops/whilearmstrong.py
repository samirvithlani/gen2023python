#153
# 1 5 3
# 1 + 125 + 27 = 153

#371
# 27 + 343 + 1 = 371

#1634 -> 1 + 1296 + 81 + 256  =1634

no = int(input("Enter a number: "))

temp2=no
count=0
while temp2>0:
    count+=1
    temp2 = temp2 // 10


rem =0
sum =0
temp = no 
#15>0 TRUE
#1>0 TRUE
while no>0:
    rem = no % 10 # 3 5 1
    sum = sum + rem**count # 27 + 125 = 152+1 = 153
    no = no // 10 # 15 // 10 = 1 1//10 = 0


if temp == sum:
    print("Armstrong number")

else:
    print("Not an armstrong number")
        