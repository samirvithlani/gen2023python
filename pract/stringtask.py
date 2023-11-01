name = "hi welcome to india"
#string
namelist = name.split(" ")
print(namelist)

#//with function
#print(max(namelist))

maxvar = namelist[0] # hi

#
for i in namelist:
    # len(hi) > len(hi) -> false
    # len(welcome) > len(hi) -> true 7>2
    # len(to) > len(welcome) -> false
    # len(india) > len(welcome) -> false
    if len(i)>len(maxvar):
        maxvar = i
        #maxvar = welcome

print(maxvar)        