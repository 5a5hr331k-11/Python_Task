# Task - 1:
def divide(x,y):
    try:
        z = x / y
    except:
        print("Error while dividing")
    else:
        print(z)
    finally:
        print("Finally statement is working")

divide(10,2)
divide(10,0)

# Task - 2:
def concatenate(a,b):
    try:
        result = a + b
    except TypeError:
        print("Error in concatenating strings")
    else:
        print(f"concatenate:{result}")
concatenate("Hello","World")
concatenate("Hello",123)

# Task - 3:
def concStr(x,y):
    strX = type(x)
    strY = type(y)
    if strX == strY:
        try:
            strZ = strX + strY
        except:
            print("Error in concatenating")
        else:
            print(strZ)
    else:
        print("String value missing")
concStr("Hello","World")
concStr("Hello",123)


