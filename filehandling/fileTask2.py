def writeData():

    file = open("filehandling/movie.txt", "a")

    file.write("The Matrix, 1999, 136 min, 8.7\n")
    file.write("The Godfather, 1972, 175 min, 9.2\n")
    file.write("The Dark Knight, 2008, 152 min, 9.0\n")
    file.write("Pulp Fiction, 1994, 154 min, 8.9\n")
    file.write("Schindler's List, 1993, 195 min, 8.9\n")

    file.close()


movies =[]
def readData():
    file = open("filehandling/movie.txt", "r")
    data = file.readlines()
    print(data)
    for i in data:
        movies.append(i.split(",")[0])

 

readData()        
print(movies)       
    
        