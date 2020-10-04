def isLucky(n):
    s, p = 0, 0
    n = str(n)
    j = len(n)
    for i in range(j // 2):
        s += int(n[i])
        p += int(n[j-1])
        i += 1
        j -= 1
    if s == p:
        return True
    else:
        return False
    
print (isLucky(239017))
