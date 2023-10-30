users = ["ram","shyam","neha","sita","gita"]
filusers = []

for i in users:
    if len(i)>3 and i.startswith("s"):
        filusers.append(i)

print(filusers)        