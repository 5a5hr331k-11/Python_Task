#nested operators

userName= "Demo"
password= "Demo123"

user= input("enter username")
userpass= input("enter password")

if userName == user:
    if password == userpass:
        print("login successful")
        if password != userpass:
            print("incorrect password")
            if userName != user:
                print("incorrect username")

if userName != user and password != userpass:
    print("incorrect username and password")
            
            


