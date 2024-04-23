# Odd or Even

n1= input("enter a number")
n1= int(n1)

if n1 % 2 == 0:
    print("the number is even")

else:
    print("the number is odd")

# Login

userName= "demo"
passWord= "d1234"

user= input("enter username")
userpass= input("enter password")

if user == userName and userpass == passWord:
    print("login successful")

elif user == userName and userpass != passWord:
    print("incorrect password")

elif user != userName and userpass == passWord:
    print("incorrect username")

else:
    print("incorrect username and password")

# Greatest of 3 numbers (a1 != a2 != a3)

a1= input("enter a1")
a2= input("enter a2")
a3= input("enter a3")

a1= int(a1)
a2= int(a2)
a3= int(a3)

if a1 > a2 and a3:
    print("a1 is greater")

elif a3 > a2 and a1:
    print("a3 is greater")

elif a2 > a3 and a1:
    print("a2 is greater")

# Displaying triangle types

side1= input("enter side 1")
side2= input("enter side 2")
side3= input("enter side 3")

side1= int(side1)
side2= int(side2)
side3= int(side3)

if side1 == side2 == side3:
    print("it is an equilateral triangle")

elif side1 == side2 or side2 == side3 or side3 == side1:
    print("it is an isoceles triangle")

else:
    print("it is a scalene triangle")

# Grade system

mark= input("enter your mark")
mark= int(mark)

if mark < 35:
    print("F Grade")

elif 35 <= mark < 45:
    print("D Grade")

elif 45 <= mark < 65:
    print("C Grade")

elif 65 <= mark < 75:
    print("B Grade")

elif 75 <= mark <= 80:
    print("A Grade")




    



