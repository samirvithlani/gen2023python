email ="  raj@gmail.com "
print(email)
print(len(email))
#strip, lstrip, rstrip

# email = email.strip()
# print(email)
# print(len(email))

# email = email.lstrip()
# print(email)
# print(len(email))

email = email.rstrip()
print(email)
print(len(email))


def isValid(name):
    name = name.strip()
    if len(name)>3:
        return True
    
    return False

password = "  am  "

if isValid(password):
    print("valid password")

else:
    print("invalid password")    










