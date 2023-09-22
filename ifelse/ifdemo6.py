#online trascatio
amount = int(input("Enter amount: "))
otp = int(input("Enter OTP: "))
bank_bal = int(input("Enter bank balance: ")) 

if otp == 123:
    print("OTP is correct")
    
    if amount > bank_bal:
        print("Insufficient balance")
    else:
        print("Transaction successful")    

else:
    print("OTP is incorrect")        