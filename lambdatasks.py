# square of a number:
sqr = lambda a : a ** 2
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
Max = lambda x,y : f"{y} is greater than {x}" if x < y else f"{x} is greater than {y}"
print(Max(int(input("enter any number")),int(input("enter another number"))))

