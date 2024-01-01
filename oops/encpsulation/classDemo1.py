class Person:
    
    def getStudentData(self): #self -> per
        print("This is a getstudent method")
        print("self..",self)



per = Person() # Creating an object of Person class        
per.getStudentData() #per.getStudentData() # Calling the method using the object it will pass current object as a parameter
print("per...",per)