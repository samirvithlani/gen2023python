'''
    [],(),{},{} set({})
    set:
    1) set is a collection of unique elements
    2) set is mutable
    3) set is unordered
    4) set is iterable
    5) set is unindexed
    6) set is represented by {}
    7) set is a collection of elements
'''
#[1000] 100th 
''''
    [10,20,30] -> 2 --> 200 10
    [10,20,200,30]

'''

# users = set({})
# print(type(users))
# print(users)

users = set({10,20,30,10,34,33,56,78,9,10,20,100})
print(users)

# for  i in users:
#     print(i)

users.add(1000)
print(users)

users.remove(108)

print(users)

