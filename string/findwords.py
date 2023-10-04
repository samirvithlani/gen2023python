sent = input("enter string: ")
count=0
for i in sent:
    if i == " ":
        count+=1

print("words = ",count+1)        