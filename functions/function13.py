# def printData(**kwargs):
#     print(kwargs)


# printData(name="surya",age=20,city="hyd")    



#function (no) -->10 {1:1,2:2:,3:3}


def genDict(no):    
    return {i:i for i in range(1,no+1)}

print(genDict(10))