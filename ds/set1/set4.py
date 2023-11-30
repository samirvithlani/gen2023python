contacts1 = set({"amit","ajay","ravi","raj","jay","raj"})
contacts2 = set({"amit","ajay","rahul"})

#contacts.remove("amita")
#contacts.discard("amita")

con3 = contacts1.union(contacts2)
print(con3)

con4 = contacts1.intersection(contacts2)
print(con4)


con5 = contacts1.difference(contacts2)
print(con5)

con6  = contacts2.difference(contacts1)
print(con6)


con7 = contacts1.symmetric_difference(contacts2)
print(con7)