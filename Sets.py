Set = {"Hello",True,123}
print(Set)
print(type(Set))
print(len(Set))

#holds multiple values in a single variable
#it is unordered, unindexed and unchangeable
#it doesn't allow duplicate values
#Note: Here, True = 1 and False = 0. Hence they're considered as duplicate values

#Set constructor:
construct = set(("Hello",True,123))
print(construct)
print(type(construct))

#Accessing set items

#i)Looping:
for x in Set:
    print(x)

#ii)in and not in:
print(1 in Set)
print("Hello" not in Set)

#Set methods

#i)add():
Set.add(False)
print(Set)

#ii)update():
My_Set = {"football","cricket"}
Set.update(My_Set)
print(Set)

myList = [12,96,45,7,18]
Set.update(myList)#can also be used to add other iterables
print(Set)

#iii)remove():
Set.remove(123)
print(Set)

#iv)discard():
Set.discard("Hello")
print(Set)

#v)pop():
random = Set.pop()
print(random)
print(Set)

#vi)clear():
My_Set.clear()
print(My_Set)

#vii)del()
del Set
print(Set)#shows error

