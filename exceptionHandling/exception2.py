data = [10,20,30,40,50]

try:
    data.remove(100)
except ValueError as e:
    print(e)    