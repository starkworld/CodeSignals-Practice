import collections


# code for (T, T+59)
def droppedRequests(requestTime):
    if len(requestTime) <= 3: return 0
    count = collections.Counter(requestTime)
    lookup = collections.defaultdict(int)
    for i in range(requestTime[0], requestTime[-1] + 1):
        lookup[i] = lookup[i - 1] + count[i]
    for i in range(3, len(requestTime)):
        temp1, temp2 = 0, 0
        if requestTime[i] - 10 in lookup: temp1 = lookup[requestTime[i] - 10]
        if requestTime[i] - 60 in lookup: temp2 = lookup[requestTime[i] - 60]
        if requestTime[i - 3] == requestTime[i]:
            requestTime[i - 3] = '$'
        elif i + 1 - temp1 > 20:
            requestTime[i] = '$'
        elif i + 1 - temp2 > 60:
            requestTime[i] = '$'
    return requestTime.count('$')


# code for (T, t-59)

def droppedRequest(requestTime):
    dropped = 0
    # this is to keep track of any of the element that is already dropped due to any of 3 limit violation.
    already_dropped = {}

    for i in range(len(requestTime)):
        if i > 2 and requestTime[i] == requestTime[i - 3]:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

        elif i > 19 and requestTime[i] - requestTime[i - 20] < 10:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

        elif i > 59 and requestTime[i] - requestTime[i - 60] < 60:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

    return dropped

print(droppedRequest([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]))

#print(droppedRequests([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]))