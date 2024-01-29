file = open("./filehandling/emp.txt", "r")

# data = file.read()  # Read the entire file
# print(data)

for i in file:
    print(i, end="")