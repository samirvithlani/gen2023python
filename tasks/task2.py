no = int(input("enter no"))
temp =no
sum=0
rem=0

while no >0:
    rem = no % 10
    sum = sum + rem**3
    no = no // 10


if temp == sum:
    print("armstrong")
else:
    print("not armstrong")        