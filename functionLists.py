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

#Task - 4:
def CountNum(myList):
    length = 0
    for count in myList:
        length += 1
    return length
print(CountNum(myList))

