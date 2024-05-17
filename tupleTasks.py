#Task 1:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple)

#Task 2:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple[1])

#Task 3:
my_Tuple = ("apple","banana","cherry")
convert = list(my_Tuple)
convert[1] = "orange"
my_Tuple = tuple(convert)
print(my_Tuple)

#Task 4:
x = (1,2,3)
y = ("a","b","c")
x += y
print(x)

#Task 5:
my_Tuple = ("apple","banana","cherry")
if "apple" in my_Tuple:
    print("yes")
else:
    print("no")

#Task 6:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple.index("cherry"))

#Task 7:
my_Tuple = ("apple","banana","cherry")
print(my_Tuple.count("banana"))

#Task 8:
singleELE = ("hello",)
print(type(singleELE))

#Task 9:
my_Num = (1,2,3,4)
convert = list(my_Num)
convert.reverse()
my_Num = tuple(convert)
print(my_Num)

#Task 10:
myTuple = ("a","b","c")
print(myTuple[-1])

#Task 11:
Tuple = ("a","b","c","d")
print(Tuple[1:3])

#Task 12:
myNumb = ("x","y")
multiply = myNumb*3
print(multiply)

#Task 13:
my_Tuple = ("apple","banana","cherry")
print(len(my_Tuple))

#Task 14:
Num1 = (1,2,3)
Num2 = (4,5,6)
if Num1 == Num2:
    print("Yes")
else:
    print("No")

#Task 15:
my_data = (10,20,30,40,50,23)
Max = max(my_data)
print(Max)

#Task 16:
myData = (-10,-20,-30,-40,-50)
Min = min(myData)
print(Min)

#Task 17:
Bool = (True,True,False)
All = all(Bool)
print(All)

#Task 18:
Bool = (True,True,False)
Any = any(Bool)
print(Any)

#Task 19:
NumbTuple = (5,2,8,1,9)
conv = list(NumbTuple)
conv.sort()
NumbTuple = tuple(conv)
print(NumbTuple)

#Task 20:
Data1 = (1,2,3)
Data2 = (4,5,6)
Data3 = Data1 + Data2
print(Data3)

