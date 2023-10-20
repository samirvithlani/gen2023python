emps = {"amit":12000, "sumit":15000, "tom":12000, "jer":20000}
emps1={i:j for i,j in emps.items() if j>10000 and len(i)>3}
# for i,j in emps.items():
#     #12000
#     if j>10000:
#         #emps["amit"] = 12000
#         #emps1["sumit"]=15000
#         emps1[i] = j



# for i,j in emps.items():
#     if len(i)>3 and j>10000:
#         emps1[i] = j
        


print(emps1)        
