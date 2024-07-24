def appreciation(func):
    def printer():
        print("You")
        func()
        print("Amazing!!!")
    return printer

@ appreciation
def tell():
    print("Are")
tell()
