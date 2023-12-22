marks = [121,23,44,56,67,32,44,90]
# 121 = "121"


palindromeMarks =  list(filter(lambda x: str(x) == str(x)[::-1],marks))
print(palindromeMarks)


#hetrogenous data

data = ["ram","shyam",100,23,"geeta",True,12.34]
strlist  = list(filter(lambda x: type(x)==str,data))
print(strlist)