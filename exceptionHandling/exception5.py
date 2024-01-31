class InvalidStringError(Exception):
    def __init__(self, value):
        super().__init__(value)


name = input("Enter your name: ")

try:
    for i in name:
        if " " in i:
            raise InvalidStringError("Name cannot contain space")
except InvalidStringError as e:
    print(e)            

else:
    print("Name is: ", name)
        

        