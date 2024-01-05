class Area:
    
    def __init__(self,h,w,r): #local variable
        print("Constructor is called param..")
        self.height = h
        self.width = w
        self.radius = r
        
    def getCircleArea(self):
        print(self.radius)
        print("Circle Area is ",3.14*self.radius*self.radius)



a1 = Area(10,20,20)      
a1.getCircleArea() # Circle Area is   
#a  = Area() # TypeError: __init__() missing 3 required positional arguments: 'h', 'w', and 'r'

a2 = Area(10,20,5)
a2.getCircleArea() # Circle Area is  78.5




        
         
        
        