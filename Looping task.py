#Task 1

for number in range(1,16,1):
    print(number)

#Task 2

for odd in range(7,30,2):
    print(odd, "odd no.")

#Task 3

for even in range(20,41,2):
    print(even, "even no.")

#Task 4

for d in range(1,16,1):
    if d % 3 == 0:
        print(d,"divisible by 3")

    elif d % 5 == 0:
        print(d,"divisible by 5")

    elif d % 5 == 0 and d % 3 == 0:
        print(d,"divisible by both 3 and 5")

    else:
        print(d,"nil")

#Task 5

l=["cricket" ,"basketball" ,"tennis" ,"badminton" ,"volleyball" ]
for sports in l:
    print(l,"sport")

#Task 7

sum=0
for x in range(1,101,1):
    sum=sum+x
    print(x)

        
