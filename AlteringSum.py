def alternatingSums(a):
    summ = 0
    summmm = 0
    for i in range(len(a)):
        if i % 2 == 0:
            summ += a[i]
        else:
            summmm += a[i]
    return summ, summmm
