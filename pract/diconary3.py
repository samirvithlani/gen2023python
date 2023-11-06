choice =-1
users ={} # empty dict
while True:
    k = int(input("Enter key: "))
    v = input("Enter value: ")
    users.update({k:v})
    choice = int(input("Do you want to continue? 0/1: "))
    if choice == 0:
        break


print(users)    