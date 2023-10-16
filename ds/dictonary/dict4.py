students = {"c1":["raj","jay","amit"],"c2":["kajal","janvi","kajal"]}

print(students)

for k,v in students.items():
    print(k)
    for j in v:
        print(j)
    print("**************")    
    