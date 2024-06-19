# square of a number:
sqr = lambda x : x ** 2
print(sqr(int(input("enter any number"))))

# checking if a number is even:
eve = lambda num : num % 2 == 0
print(eve(int(input("enter any number"))))

# concatenate two strings:
string = lambda Str1, Str2 : Str1 + " " + Str2
print(string((input("enter any string")),(input("enter another string"))))

# Sum of three numbers:
Sum = lambda n1 , n2 , n3 : n1 + n2 + n3
print(Sum(int(input("enter number 1")),int(input("enter number 2")),int(input("enter number 3"))))

# Maximum of two numbers:
Max = lambda a , b : a if a > b else b > a
print(Max(int(input("enter any number")),int(input("enter any number"))))
