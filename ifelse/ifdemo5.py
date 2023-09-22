age =int(input("Enter your age: ")) # 18
police_cases = int(input("Enter number of police cases: ")) # 2
term_plan = int(input("Enter term plan: ")) # 0 for yes and 1 for no
bank_balance = int(input("Enter bank balance: ")) # 1000000

police_cases_allowed = 2

if age>=18:
    print("you are eligible for age criteria")
    
    if police_cases<=police_cases_allowed:
        print("you are eligible for police cases criteria")
        
        if term_plan ==0:
            print("you are eligible for term plan criteria")
            
            if bank_balance>1000000:
                print("you are eligible for bank balance criteria")
            else:
                print("you are not eligible for bank balance criteria")
                    
        else:
            print("you are not eligible for term plan criteria")
                
    else:
        print("you are not eligible for police cases criteria")
            
    
    
else:
    print("you are not eligible for age criteria")    