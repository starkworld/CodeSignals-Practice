def firstDuplicate(a):
    found = {}
    for num in a:
        if num in found:
            return num
        else:
            found[num] = 1
    return -1


# First non repeating Character
def firstNotRepeatingCharacter(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1:
            return char
    return '_'


print(firstDuplicate('andcda'))

print(firstNotRepeatingCharacter('andcda'))
