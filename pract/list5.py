users =[] #empty list
x= ""
choice =0   
while True:
    x = input("enter name")
    users.append(x)
    choice = int(input("do you want to continue? 1 for yes 0 for no"))
    if choice == 0:
        break

print(users)    