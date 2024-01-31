def storePalindromoe(data):
    file = open("./palin.txt", "w")
    
    for i in data:
        if i == i[::-1]:
            file.write(i + "\n")
    file.close()
  
storePalindromoe(["madam", "malayalam", "python", "java", "c", "c++", "php", "nitin"])    
            