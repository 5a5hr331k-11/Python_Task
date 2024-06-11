#Task - 1:
def createset():
    print(set((7,34,12,77,3)))
createset()

#Task - 2:
numSet = {11,18,2,3,26,10,8}
def loopSet(iterate):
    for x in numSet:
        print(x)
        x += 1
loopSet(numSet)

#Task - 3:
def addAllnum(total):
    sum = 0
    for add in total:
        sum += add
    return sum
print(addAllnum(numSet),"is the sum of all numbers in the set")

#Task - 4:
def removeAllnum(Empty):
    Empty.clear()
    print(Empty)
removeAllnum(numSet)

#Task - 5:
numSet = {11,18,2,3,26,10,8}
num2Set = {23,10,7,8,18,45,93} 
def removeEle(Remove):
    for num in Remove:
        if num in num2Set:
            Remove.remove(num)
            
            print(Remove)
removeEle(numSet)
        
#Task - 6: 
numSet = {11,18,2,3,26,10,8}        
num2Set ={23,10,7,8,18,45,93} 
def interset(intersect):
    n = intersect.intersection(num2Set)
    print(n)
interset(numSet)




    
