class Eletronics:
    
    def __init__(self):
        print("Eletronics class constructor")
        self.productName = "tv"
        self.price = 2300.90
    def elecMethod(self):
        print("Eletronics class method")    



class Tv(Eletronics):
    
    def __init__(self):
        super().__init__()  # Calling parent class constructor
        self.color = "black"        
        
    def getTvData(self):
        print("Product Name: ", self.productName)
        print("Price: ", self.price)
        print("Color: ", self.color)    
        

t = Tv() #default constructor of Tv class will be called        
t.getTvData() # Calling method of Tv class
t.elecMethod() # Calling method of Eletronics class