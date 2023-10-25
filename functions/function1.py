def test():
    print("test function called...")
    print("wo return type without args")

test()#function call    

#give explicit return type None

def test1() -> None:
    print("test1 function called...")


test1()#function call    


def add(a,b):
    print("add function called...")
    # c = a+b
    # return c
    return a+b

ans = add(10,20)#function call
print("ans = ",ans)



def mul():
    no = int(input("Enter no: ")) #local variable
    return no**2

x = mul()
print("x = ",x)

#print(no) #error