file = open("./filehandling/emp.txt", "r")

data = file.readlines()  # Read the entire file
print(data)

for i in data:
    print(i, end="")



