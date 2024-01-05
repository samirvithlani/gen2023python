class Bank:
    
    balance = 1000
    
    
    def __init__(self):
        print("Constructor is called")
        self.balance = 0  # instance variable,public variable
        self.name = "SBI"
        self.branch = "Mumbai"
    
    def __del__(self):
        print("Destructor is called")
        #callaoc and malloc in c/c++ delete free in c++
        self.balance = 0
        self.name = ""
        self.branch = ""
            




b = Bank() # Constructor is called
print(b.name)
print(b.balance)
print(Bank.balance)
        
    