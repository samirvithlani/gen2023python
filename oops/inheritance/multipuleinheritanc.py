#1 parent class n child class
#n parent class 1 child class

class Andorid:
    
    def __init__(self):
        print("Andorid class constructor")
        self.os = "Android"
        self.version = 11

class Samsung(Andorid):
    
    def __init__(self):
        super().__init__()
        self.brand = "Samsung"
        self.model = "Galaxy S24"
        self.price = 123455
        
    def getMyPhone(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)
        print("OS: ", self.os)
        print("Version: ", self.version)
            
class Oppo(Andorid):
    
    def __init__(self):
        super().__init__()
        self.brand = "Oppo"
        self.model = "Oppo F19"
        self.price = 30000
    def getMyPhone(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)
        print("OS: ", self.os)
        print("Version: ", self.version)
        


op = Oppo()
op.getMyPhone()            