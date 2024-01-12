class TRAI:
    
    def __init__(self):
        print("TRAI constructor")
    
    def call(self):
        print("TRAI call method")    
        
    #pure virtual method
    
    #virtual def call1 =0


class JIO(TRAI):
    
    def __init__(self):
        super().__init__()
        print("JIO constructor")
    
    def call(self):
        #super().call()
        print("JIO call method")            
        


j = JIO()
j.call()        