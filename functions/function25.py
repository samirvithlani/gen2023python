def isValid(func):#func =vote
    age =1
    def inner():
        if age>=18:
            func()
        else:
            print("Not eligible")

    return inner


@isValid
def vote():
    print("Eligible to vote")                


vote()    