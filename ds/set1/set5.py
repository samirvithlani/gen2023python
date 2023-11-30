contacts1 = set({"amit","ajay","ravi","raj","jay","raj"})
contacts2 = set({"amit","ajay","rahul"})

print(contacts1)
#contacts1.difference_update(contacts2) it update in new ser
contacts1.difference_update(contacts2) #it update in same set
print(contacts1)

#contacts1.intersection_update(contacts2)
#contacts1.symmetric_difference_update(contacts2)