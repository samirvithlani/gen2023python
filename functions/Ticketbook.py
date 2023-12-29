import random
import string

ticketPrice = 1000
passangerDetails = []

#create Decorator for checking the availability of seats

def generateNumber():
    len = 10
    randomdString = "".join(random.choice(string.ascii_uppercase + string.digits)for i in range(len))    
    return randomdString

    
    

def payment(noOfTickets):
    print("***************Payment function******************")
    totalPrice = noOfTickets * ticketPrice
    print("Total price: ",totalPrice)
    return totalPrice

def bookTicket():
    
    
    noOfTotalSeats = 100
    noOfAvailableSeats = 100
    print("Book ticket function")
    print("How many tickets you want to book?")
    bookTicketCount = int(input("Enter ticket count: "))
    
    if bookTicketCount > noOfAvailableSeats:
        print("Sorry,  seats are available only ", noOfAvailableSeats)
    else:
        for i in range(1,bookTicketCount+1):
            print("Enter passanger details")
            havingVisa  = bool(input("Having visa? "))  #if visa is true then only he can travel
            name = input("Enter name: ")
            age = int(input("Enter age: ")) #no criteria for age
            gender = input("enter gender") 
            contactNo = input("Enter contact number: ")
            passportNo = input("Enter passport number: ")
    
            data = {}
            data["havingVisa"] = havingVisa
            data["name"] = name
            data["age"] = age
            data["gender"] = gender
            data["contactNo"] = contactNo
            data["passportNo"] = passportNo
        
            #passangerDetails.append(data)
    
    paymentAmount = payment(bookTicketCount)
    if(paymentAmount>0):
        print("Payment successfull")
        print("Payment amount: ",paymentAmount)
        print("Ticket booked successfully")
        data["ticketNo"] = generateNumber()
        print("Ticket number: ",data["ticketNo"])
        data["ticketPrice"] = paymentAmount
        data["ticketStatus"] = "Booked"
        passangerDetails.append(data)
        print("Passanger details: ",passangerDetails)
        
        noOfAvailableSeats = noOfAvailableSeats - bookTicketCount
    else:
        print("Payment failed")            

def getTicketStatus():
    print("Get ticket status function")
    #print("ticekt Data",passangerDetails)
    ticketNo = input("Enter ticket number: ")
    #[{},{},{}]
    for i in passangerDetails:
        print("i",i)
        if(i["ticketNo"]==ticketNo):
            print("Matched....")
    
           


while True:
    print("Bus ticket booking")
    print("1. Book ticket")
    print("2. Cancel ticket")
    print("3. Get ticket status")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if(choice ==1):
        bookTicket()
    elif(choice ==2):
        print("Cancel ticket")
    elif(choice ==3):
        getTicketStatus()
    else:
        print("Exit")
        break
                    