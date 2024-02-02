def loginRequired(func):#accessDb
    def inner(data):#{"login":True,"name":"amit"}
        if data["login"]==True:
            func(data)
        else:
            print("You are not logged in")    
    
    return inner        


@loginRequired
def accessDb(data):
    print("Accessing the database")
    print("Name:",data["name"])
    

accessDb({"login":True,"name":"amit"})    
