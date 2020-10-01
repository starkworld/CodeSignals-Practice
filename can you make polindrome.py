from collections import Counter


def giveCounterlist(s):
    cnt = Counter()
    cntlist = [cnt]
    # Calculating odd and even count for every string of the form s[0],s[0]+s[1],s[0]+s[1]+s[2]- - - -,-----+s[-1]
    for i in s:
        cnt[i] += 1
        cnt[i] = cnt[i] % 2
        cntlist.append(cnt)

    return cntlist


def givequeryans(cntlist, i, j, k):
    cnt = cntlist[j + 1] - cntlist[i]  # Counter for given query
    # If total number of elements with odd count/2 are more than k then it's impossible to make a palindrome
    # otherwise we can make a palindrome string
    return 1 if sum(abs(i) for i in cnt.values()) // 2 <= k else 0


# Input (string size,number of queries and string)
n, q = [int(i) for i in input().split()]
s = input()

# Resultant answer string
ans = ""
cntlist = giveCounterlist(s)  # Counter List

for i in range(q):
    # Input (k,left index and right index)
    k = int(input())
    l, r = [int(j) for j in input().split()]

    ans += str(givequeryans(cntlist, l, r, k))

print(ans)