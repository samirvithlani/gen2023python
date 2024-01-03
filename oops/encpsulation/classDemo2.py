class User:
    
    # def userDetail(self): #self is a current object of class
    #     salary = 1000 # local variable
    #     self.name = "raj" # instance variable
    #     self.age = 23                  #copy of instnace variable will be created for every object  
    #     self.address = "Delhi"
    
    country = "India" # class variable, static variable, -->1 copy....
    
    def userDetail(self,name,age,address): #self is a current object of class 
        self.name = name # instance variable u1.name
        self.age = age                 
        self.address = address
    
    
    def showUserDetail(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Address : ",self.address)
        print("Country",User.country) # accessing class variable    
        #print("Salary : ",salary) # NameError: name 'salary' is not defined
        



u1 = User()
u1.userDetail("amit",34,"Delhi")        
u1.showUserDetail()
u2 = User()
u2.userDetail("parth",35,"Delhi")
u2.showUserDetail()
print("u1...",u1.name)
print(User.country)