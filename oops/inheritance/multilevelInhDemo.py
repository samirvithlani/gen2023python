class Gov:
    
    def __init__(self):
        print("Gov class constructor")
        self.party = "BJP"
        self.pm = "Narendra Modi"


class StateGov(Gov):
    
    def __init__(self):
        
        super().__init__()
        print("StateGov class constructor")
        self.state = "Guajrat"
        self.stateCapital = "Gandhinagar"
        self.stateCM = "Bhupendra Patel"

    def getGovProp(self):
        print("Party: ", self.party)
        print("PM: ", self.pm)


class AMC(StateGov):
    
    
    def __init__(self):
        super().__init__()     
        self.city = "Ahmedabad"
        self.tax = 12.5
        
    def getMyCityData(self):
        print("City: ", self.city)
        print("Tax: ", self.tax)
        print("State: ", self.state)
        print("State Capital: ", self.stateCapital)
        print("State CM: ", self.stateCM)
        print("Party: ", self.party)
        print("PM: ", self.pm)


a = AMC()
a.getMyCityData()               


                