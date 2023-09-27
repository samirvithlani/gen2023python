#sum of digit..  123 --> 1+2+3 = 6
# 123 % 10 = 3 
# 12 % 10 = 2
# 1 % 10 = 1

#123 // 10 = 12
#12 // 10 = 1
#1 // 10 = 0

no = int(input("Enter a number: ")) 
rem=0
sum=0
while no!=0:
    rem = no % 10
    sum = sum + rem
    no = no // 10
    
print("sum of digits is: ",sum)