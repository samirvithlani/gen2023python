no = int(input("enter no :"))
#5 -- 5 * 4 * 3* 2 *1 => 120
#  1  *2 * 3 * 4 * 5 --> 120
# 1 to no 1 to 5 0--> 1 2 3 4 

mul =1
for i in range(1,no+1):
    #1 = 1 * 1 = mul =1
    #1 = 1 *2 = mul=2
    #2 = 2 * 3 = mul =6
    #6 = 6 * 4 = mul =24
    #24 = 24 * 5 = mul 120
    mul = mul * i


print(mul)    