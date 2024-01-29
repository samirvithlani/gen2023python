age = 18
name = "ram"


file = open("./filehandling/emp.txt","a")
print("age = ",age,file=file)
print("name = ",name,file=file)
file.write("age = "+str(age)+"\n")
file.close()

