class User:
    
    @staticmethod
    def userData(self):
        print("This is a static method")
    
    @classmethod    
    def printUserData(self):
        print("This is a normal method")    


u = User()
u.userData() # TypeError: userData() takes 0 positional arguments but 1 was given        
#User.userData() # This is a static method