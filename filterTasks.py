# Task - 1:
int_num = [-2,-1,0,1,2]

def displayPositive(z):
    return 0 < z
print(list(filter(displayPositive,int_num)))

positiveList = list(filter(lambda x : x > 0,int_num))
print(positiveList)

# Task - 2:
vowelList = ["a","e","i","o","u"]
def display_vowels(characters):
    return characters in vowelList
alphabets = ["a","b","c","d","e","f","g","h","i"]
print(list(filter(display_vowels,alphabets)))

is_vowel = list(filter(lambda a : a in alphabets,vowelList))
print(is_vowel)

# Task - 3:
peopleAge = {
    "user1" : 13,
    "user2" : 17,
    "user3" : 25,
    "user4" : 31
}
