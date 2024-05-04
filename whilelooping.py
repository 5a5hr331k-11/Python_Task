#Task 1
n=0
while n<15:
    n+=1
    print(n,"number")

#Task 2
i=5
while i<29:
    i+=2
    print(i,"odd")

#Task 3
eve=18
while eve<40:
    eve+=2
    print(eve,"even")

#Task 4
num=0
while num<15:
    num+=1
    if num%3==0 and num%5==0:
        print(num,"divisible by 3 and 5")
    elif num%3==0:
        print(num,"divisible by 3")
    elif num%5==0:
        print(num,"divisible by 5")
    else:
        print(num)

#Task 5
List=["Hands","Head","Legs"]
p=0
while p < len(List):
   print(List[p])
   p+=1

#Task 6
Sum = 0
n = 0
numbers = [3,18,10,26]
while n < len(numbers):
    Sum = Sum + numbers[n]
    n += 1
    print(Sum)

#Task 7
Sum = 0
z = 0
while z < 100:
    Sum = Sum + z
    z += 1
    print(Sum)

#Task 8
n = input("enter any number")
n = int(n)
f = 1
while n >= 1:
    f *= n
    n -= 1
    print(f)


