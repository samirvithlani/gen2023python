from multipledispatch import dispatch

class Amazone:
    
    def __init__(self):
        print("Amazone constructor")
    
    
    @dispatch()
    def search(self):
        print("Amazone search method")
    
    @dispatch(str)
    def search(self, item):
        print("Amazone search method with item", item)        
    
    @dispatch(str, int)
    def search(self, item, quantity):
        print("Amazone search method with item", item, "and quantity", quantity)    
        
    @dispatch(list) 
    def search(self,productList):
        print("Amazone search method with product list", productList)
        


a = Amazone()
#a.search()
# a.search("Mobile")        
# a.search("Mobile", 2.2)
a.search(["Mobile", "Laptop", "TV"])
a.search("mobile")