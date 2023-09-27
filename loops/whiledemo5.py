# amount = int(input("Enter amount:"))
# while amount<10000:
#     print("Amount is less than 10000")
#     amount = int(input("Enter amount:"))


# print("Amount is:",amount)        
amount =0
chances = 2
while True:
    if(chances>0):
        amount = int(input("Enter valid  amount *10000 :"))
        if(amount>=10000):
            break
        else:
            chances = chances - 1
    else:
        break        

print("Amount is:",amount)    
    
    
