data = "hi this is India welcome to India"

x = data.split(" ")
print(x)

maxvar = x[0]
#hi

for i in x:
    #hi > hi
    # this > hi
    # is > this
    # India > this
    # welcome > India
    # to > welcome
    # India > welcome
    
    if len(i) > len(maxvar):
        #this
        #India
        #welcome
        maxvar = i

print(maxvar)        

#print(max(x))

email ="raji@gmail.com"

x1 = email.split("i")
print(x1)

