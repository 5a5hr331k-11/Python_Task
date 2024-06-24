from functools import reduce

# Task - 1:

def sum_elements(x , y):
    return x + y
total = reduce(sum_elements, [2,7,5,4,9])
print(total)

# Task - 2:
def multiply_elements(a , b):
    return a * b
product = reduce(multiply_elements, [2,7,5,4,9])
print(product)

# Task - 3:
def flatList(str1 , str2):
    return str1 + str2
Flatten = reduce(flatList, [["H"],["e"],["l"],["l"],["o"]])
print(Flatten)

# Task - 4:
def Fact_elements(num , n):
    return num*n
num = int(input("enter any number"))
Factorial = reduce(Fact_elements, range(1,num+1))
print(Factorial)

# Task - 5:
def Max_element(p , q):
    return p if p > q else q
Maximum = reduce(Max_element, [2,7,5,4,9])
print(Maximum)

# Task - 6:
def concatenate_str(str1 , str2):
    return str1 + str2
Join = reduce(concatenate_str, ["Hello","World"])
print(Join)
