def checkString(name,l):
    name = name.strip()
    if len(name)>l:
        return True
    
    return False


# x = checkString("    kjak")
# print("x = ",x)

if checkString("java",4):
    print("valid string")
else:
    print("invalid string")    