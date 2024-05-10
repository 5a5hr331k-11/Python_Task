#Task 1
Sum = 0
myList = [2,3,18,10,26]
for x in range(0,len(myList)):
    Sum += myList[x]
    print(Sum)

#Task 2
myList = [2,3,18,10,26]
myList.sort()
print(myList[-1],"is the largest number")

#Task 3
myList = [2,3,18,10,26]
myList.sort()
print(myList[0],"is the smallest number")

#Task 4
myList = [2,3,18,10,26]
print(len(myList))

#Task 5
myList = [2,3,18,10,26]
myList.reverse()
print(myList)

#Task 6
noneList = []
if len(noneList)== 0:
    print("the list is empty")
else:
    print("the list is full")

#Task 7
dupeList = [1,1,3,5,5,7]
empList = []
for n in dupeList:
    if n not in empList:
        empList.append(n)
        print(empList)

#Task 8
myList = [2,3,18,10,26]
noList = []
for m in myList:
    if m % 2 == 0:
        noList.append(m)
        print(noList)
    
