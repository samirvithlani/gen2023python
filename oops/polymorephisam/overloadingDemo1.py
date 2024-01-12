class Zomato:
    
    def __init__(self):
        print("Zomato constructor")
    
    
    def order(self):
        print("Zomato order method")
    
    
    def order(self, item):
        print("Zomato order method with item", item)
        
    def order(self, item, quantity):
        print("Zomato order method with item", item, "and quantity", quantity)



z = Zomato()
z.order(100,2)                    
    