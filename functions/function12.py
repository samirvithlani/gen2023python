def convertList(*args):
    
    #return [i.upper() for i in args if type(i) == str]
    return [i.upper() if type(i) == str else i for i in args]

x = convertList("python","java","c","c++",10)
print(x)


#len less thn 4 upper case and  and grt 5 title case...

def convertList2(*args):
    
    #return [i.upper() if type(i) == str and len(i) < 4 else i.title() if type(i) == str and len(i) > 5 else i for i in args]
    #return [i.upper() if len(i) < 4 else i.title() if type(i) == str and len(i) > 5 else i for i in args]
    return [i.upper() if len(i)<4 else i.title() for i in args]


x = convertList2("python","java","c","c++","scala","perl","ruby","go","swift")
print(x)