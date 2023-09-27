no = int(input("Enter a number: ")) #123-3,4567-4,123456-6

#123
# 123 // 10 = 12 1st iteration
# 12 // 10 = 1 2nd iteration
# 1 // 10 = 0 3rd iteration

#7543 -->4
#7543 // 10 = 754 1st iteration
#754 // 10 = 75 2nd iteration
#75 // 10 = 7 3rd iteration
#7 // 10 = 0 4th iteration
#while no !=0:
count=0
#123 > 0 TRUE
#12 > 0 TRUE
#1 > 0 TRUE
#0 > 0 FALSE
while no>0:
    #count = count + 1 count =1
    #count = count + 1 count =2
    #count = count + 1 count =3
    count+=1
    #no = 123 // 10 = 12
    #no = 12 // 10 = 1
    #no = 1 // 10 = 0
    no = no // 10



print("Total digits are: ",count)    