no = int(input("enter no"))

sum= 0
rem = 0

while no>0:
    rem = no % 10
    sum = sum * 10 + rem
    no = no // 10
    

print(sum)    