#prime no
no = int(input("enter no:"))
count=0
for i in range(2,no+1):
    if no % i ==0:
        count+=1


if count<=2:
    print("prime no")       

else:
    print("not prime...")    
        