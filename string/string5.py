#boolean 

data = "java hello"

x = data.isalpha()
print("is alpha -->>",x)
x = data.isdigit()
print("is digit -->>",x)
x = data.isalnum()
print("is alpha numeric -->>",x)
x = data.isspace()
print("is space -->>",x)
x = data.islower()
print("is lower -->>",x)
x = data.isupper()
print("is upper -->>",x)
x = data.istitle()
print("is title -->>",x)

# data  =data.capitalize()
# print("capitalize -->>",data)

x = data.startswith("ja")
print("startswith -->>",x)

x = data.endswith("lo")
print("endswith -->>",x)


f = data.find(" ") 
print("find -->>",f)



