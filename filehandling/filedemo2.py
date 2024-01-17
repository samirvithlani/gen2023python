users = ["user1", "user2", "user3", "user4", "user5"]

with open("./filehandling/user.txt","a") as file:
    file.writelines(users)
    file.close()
    