class Gov:
    
    fees = 1000
    name = "CV"
    
    def __init__(self):
        print("Gov class constructor")
        self.AADHAR = 1234567890
        self.VOTERID = 1234567890
        self.PAN = "ABCDE1234F"
        
class School:
    
    fees = 2000
    city = "Ahmedabad"
    def __init__(self):
        print("School class constructor")
        self.schoolName = "ABC School"
        self.schoolCode = 1234
        self.schoolAddress = "Ahmedabad"
        self.schoolContact = 1234567890



class Student(Gov,School):
    
    def __init__(self):
        super().__init__()
        self.name = "raj"        
        self.rollNo = 1
        
    def getStudentData(self):
        print("fees: ", self.fees)
        print("Name: ", self.name)
        # print("Name: ", self.name)
        # print("Roll No: ", self.rollNo)
        # print("AADHAR: ", self.AADHAR)
        # print("VOTERID: ", self.VOTERID)
        # print("PAN: ", self.PAN)
        # print("School Name: ", self.schoolName)
        # print("School Code: ", self.schoolCode)
        # print("School Contact: ", self.schoolContact)    



s = Student()
s.getStudentData()                
        