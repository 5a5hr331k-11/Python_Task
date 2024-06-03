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
    
