# Task - 1:
myList = [12,45,87,1,5]
def addNum(Total):
    sum = 0
    for n in Total:
        sum += n
    return sum
print(addNum(myList))

# Task - 2:
def MaxElement(Maximum):
    Largest = Maximum[0]
    for Max in Maximum[1:]:
        if Max > Largest:
            Largest = Max
    return Largest
print(MaxElement(myList))

# Task - 3:
def MinElement(Minimum):
    Smallest = Minimum[0]
    for Min in Minimum[1:]:
        if Min < Smallest:
            Smallest = Min
    return Smallest
print(MinElement(myList))

# Task - 5:
def reverseList(Rev):
    print(Rev[::-1])
reverseList(myList)

#Task - 4:
def CountNum(myList):
    length = 0
    for count in myList:
        length += 1
    return length
print(CountNum(myList))

# Task - 6:
noneList = []
def check_emp(Empty):
    if len(noneList) == 0:
        print("The list is empty")
    else:
        print("the list is full")
check_emp(noneList)

# Task - 7:
dupList = [12,56,73,5,4]
def check_duplicate(Remove):
    for num in myList:
        if num in dupList:
            dupList.remove(num)
            print(dupList)
check_duplicate(myList)

# Task - 8:
eve_List = []
def remove_even(x):
    for eve in myList:
        if eve % 2 == 0:
            eve_List.append(eve)
            print(eve_List)
remove_even(myList)

            
        

