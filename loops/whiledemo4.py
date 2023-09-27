#reverse no:
#123 321 

no = int(input("Enter no:"))
rem=0
sum =0
temp = no
# 987  789
#987>0 true
#98>0 true
#9>0 true
while no>0:
    
    #rem = 987 % 10 = 7
    #rem = 98 % 10 = 8
    #rem = 9 % 10 = 9
    rem = no % 10 
    #sum = 0 * 10 + 7 = 7
    #sum = 7 * 10 + 8 = 78
    #sum = 78 * 10 + 9 = 789
    sum = sum * 10 + rem
    #no = 987 // 10 = 98
    #no = 98 // 10 = 9
    #no = 9 // 10 = 0
    no = no // 10
    

print(sum)    
    
    
if temp == sum:
    print("Palindrome")

else:
    print("Not a palindrome")        