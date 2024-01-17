class Vehicle:
    
    name = "AUDI"
    __version = "1.0.1" # private variable
    
    def __init__(self):
        print("Vehicle class constructor")
        self.__engine = "V8" # private variable
        self.color = "Black"
    
    def getCarData(self):
        print("Name: ", self.name)
        print("Version: ", self.__version)
        print("Engine: ", self.__engine)
        print("Color: ", self.color)



v = Vehicle()
v.getCarData()

print("Name: ", v.name)
print("Version: ", v.__version)            
    
    