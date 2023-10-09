data = [10,20,30,10,5,3,45,20]
unqdata =[]
dupdata =[]
for i in data:
    # i =10 , true
    # i =20 , true
    # 30
    # 10 false
    if i not in unqdata:
        #10,20,30
        unqdata.append(i)
    else:
        dupdata.append(i)    


print("unique data",unqdata)
print("duplicate data...",dupdata)        