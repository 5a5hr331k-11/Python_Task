#Slice:

name = "ocean academy"
print(name[1:8])

#Uppercase:

print(name.upper())

#Lowercase:

print(name.lower())

#Replace:

print(name.replace("c","l"))

#Length of string:

print(len(name))

#Strip:

x = "  ocean academy  "
print(x.strip())

#l strip:

print(x.lstrip())

#r strip:

print(x.rstrip())

#Capitalize:

print(name.capitalize())

#Split:

print(name.split( ))

#Casefold:

print(name.casefold())

#Count:

Count = "the number of offers I recieve everyday are endless"
print(Count.count("of"))

#endswith:

print(name.endswith("y"))

#startswith:

print(name.startswith("o"))

#Find:

print(name.find("aaaa"))

#Title:

print(name.title())

#Swapcase:

print(name.swapcase())

#Splitlines:

String = "the number of offers\n I recieve everyday\n are endless"
print(String.splitlines())

#Join:

myList = ["stump", "ball", "bat"]
print("and".join(myList))

#Replace:

myString = "the number of offers I recieve everyday are endless"
print(myString.replace("offers","gifts"))

#Index:

name = "ocean academy"
print(name.index("academy"))

#Isalnum:

Demo = "de123"
print(Demo.isalnum())

#Isalpha:

myDemo = "demo"
print(myDemo.isalpha())

#Isdecimal:

myNum = "18"
print(myNum.isdecimal())

#Isdigit:

myNum = "18"
print(myNum.isdigit())

#Islower:

name = "ocean academy"
print(name.islower())

#Isnumeric:

myNum = "18"
print(myNum.isnumeric())

#Partition:

myString = "the number of offers I recieve everyday are endless"
print(myString.partition("offers"))

#Zfill:

myNum = "18"
print(myNum.zfill(3))

#f-String:

price = "5"
sentence = f"the cost of the pen is {price} rupees"
print(sentence)



