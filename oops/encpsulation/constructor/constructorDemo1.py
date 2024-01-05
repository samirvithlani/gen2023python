class Bank:
    
    balance = 1000
    
    
    def __init__(self):
        print("Constructor is called")
        self.balance = 0  # instance variable,public variable
        self.name = "SBI"
        self.branch = "Mumbai"
        




b = Bank() # Constructor is called
print(b.name)
print(b.balance)
print(Bank.balance)
        
    