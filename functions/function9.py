def test(**kwargs):
    print(kwargs)
    #data = {x:x.upper() for x in kwargs}
 #   data = {x:y.upper() for x,y in kwargs.items()}
    data = {x:y**2 if y > 30 else y for x,y in kwargs.items() }
    print(data)


#test(name="raj",city="pune")
test(a=10,b=20,c=30,d=40,e=50)