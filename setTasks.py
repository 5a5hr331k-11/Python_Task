#Size of a set:
My_set = {"Football","Cricket","Basketball","Chess"}
print(len(My_set))

#Maximum and Minimum of a set:
numSet = {12,43,7,45,17}
convSet = list(numSet)
convSet.sort()
print(convSet[0],"minimum",convSet[-1],"maximum")

#Task 1:
consSet = set(("Football","Cricket","Basketball","Chess"))
print(consSet)

#Task 2:
for x in My_set:
    print(x)

#Task 3:
My_set.add("Volleyball")
print(My_set)

#Task 4:
My_set.remove("Chess")
print(My_set)

#Task 5:
numSet = set(convSet)
second_set = {7,45,89,60,34}
for item in second_set:
    if item in numSet:
           numSet.remove(item)
           print(numSet)

#Task 6:
DemoSet = {"Youtube","Twitter","Instagram","Mail"}
Demo2Set = {"Fax","Mail","Messages","Telephone"}
DemoSet.intersection(Demo2Set)
print(DemoSet)

#Task 7:
DemoSet.difference(Demo2Set)
print(DemoSet)

#Task 8:
subSet = {"Football","Cricket"}
print(subSet.issubset(My_set))

#Task 9:
print("Cricket" in consSet)

#Task 10:
if My_set.isdisjoint(DemoSet):
    print("there are no common elements")
else:
    print("there are common elements")

        




