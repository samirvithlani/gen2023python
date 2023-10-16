users = {"name":"ram","age":23,"salary":"10000","city":"hyd","isActive":True}

x = users.get("name")
print(x)

removedelm = users.pop("salary")
print("removig....",removedelm)

print(users)

x1 = users.popitem()
print("x1-->",x1)

l = len(users)
print("length ",l)

