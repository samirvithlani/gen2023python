#python
#p:p,y:Y,t:T,h:H,o:O,n:N

# data = {i:i.upper() for i in "python"}
# print(data)
# #p:p,y:yy,t:ttt,h:hhhh,o:ooooo,n:nnnnnn

string = "python"
#len 6 
#sting[i] = p: p
#stringp[i] =y : yy
#string[i] = t * 3 : ttt

data = {string[i]: string[i] * (i + 1) for i in range(0,len(string))}
print(data)








# print("p"*1)
# print("y"*2)
# print("t"*3)
# print("h"*4)
# print("o"*5)