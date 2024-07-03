import random

# random.random():

print(random.random())

# random.uniform():

print(random.uniform(1,11))

# random.randint():

print(random.randint(1,11 ))

# random.choice ():

myList = [ "bat","ball","pitch","players"]
print(random.choice(myList))

# random.shuffle():
myList = [ "bat","ball","pitch","players"]
random.shuffle(myList)
print(myList)

# random.sample():
myList = [ "bat","ball","pitch","players"]
print( random.sample(myList, k = 2))


