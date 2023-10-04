data =[]
choice = -1 # 0 for no 1 for yes
no=0

while True:
    
    choice = int(input("Do you want to continue? 0 for no 1 for yes: "))
    
    if choice == 0:
        break
    elif choice == 1:
        no = int(input("Enter no: "))
        data.append(no) #111,34
    else:
        print("Invalid choice")
        break

print("data = ", data)               
    
    