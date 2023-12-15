# def findPalindromes(names):
    
#     palindroms =[]    
    
#     for i in names:
#         if i == i[::-1]:
#             palindroms.append(i)
        
#     return palindroms


# x = findPalindromes(['madam','mom','dad','malayalam','python','java','php'])        
# print(x)

names = ['madam','mom','dad','malayalam','python','java','php']

paindromes = [i for i in names if  i == i[::-1]]
print(paindromes)            

    
    
    
    