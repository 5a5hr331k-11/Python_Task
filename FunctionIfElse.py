# Task - 1:
def OddOrEve(num):
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
OddOrEve(3)

# Task - 2:
def UserDetails(nameKey,passKey):
    Name = "Demo"
    Pass = "demo123"
    if nameKey == Name and passKey == Pass:
        print("login successful")
    elif nameKey == Name and passKey != Pass:
        print("password is incorrect")
    elif nameKey != Name and passKey == Pass:
        print("username is incorrect")
    else:
        print("both username and password are incorrect")
UserDetails(input("enter username"),input("enter password"))

# Task - 3:
def maxNum(n1,n2,n3):
    if n1 > n2 and n3:
        print("n1 is greater")

    elif n3 > n2 and n1:
        print("n3 is greater")

    elif n2 > n3 and n1:
        print("n2 is greater")
maxNum(int(input("enter n1")),int(input("enter n2")),int(input("enter n3")))

# Task - 4:
def IntNum(Integer):
    if Integer > 0:
        print("the number is positive")
    elif Integer == 0:
        print("the number is zero")
    else:
        print("the number is negative")
IntNum(int(input("enter any number")))

# Task - 5:
def Side(side1,side2,side3):
    if side1 == side2 == side3:
        print("it is an equilateral triangle")

    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("it is an isoceles triangle")

    else:
        print("it is a scalene triangle")
Side(int(input("enter side1")),int(input("enter side2")),int(input("enter side3")))

# Task - 6:
def markData(mark):
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
markData(int(input("enter student's mark")))


    
