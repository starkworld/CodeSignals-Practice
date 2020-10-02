def allLongestStrings(inputArray):
    lst = []
    a = len(max(inputArray, key=len))
    print(a)
    for i in inputArray:
        if len(i) == a:
            lst.append(i)
    return lst


print(allLongestStrings(["enyky", 
 "benyky", 
 "yely", 
 "varennyky"]))
