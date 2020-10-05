def sortByHeight(a):
    sorted_lst = sorted([x for x in a if x != -1])
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i] = sorted_lst[j]
            j += 1
    return a
