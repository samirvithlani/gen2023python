file = open("./filehandling/prod.txt", "r")

# data = file.read()  # Read the entire file
# print(data)

count = 0
for  i in file:
    count += 1
    print(i, end="")

print("Total lines in file:", count)    