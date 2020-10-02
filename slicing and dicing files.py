from idlelib.TreeWidget import TreeNode
from math import sin, cos, sqrt, atan2, radians
from typing import List

import requests

"""Account validation code Akuna Capitals"""

inp = input("enter:")
try:
    j = int(inp[:-2].upper(), 16)
except:
    print("INVALID")
else:
    k = int(inp[-2:].upper(), 16)
    summ = 0
    for i in str(j):
        summ += int(i)

    if str(hex(summ)) == str(hex(k)):
        print("Valid")
    else:
        print("Invalid")


"""Travel Distance code Akuna Capitals"""

def travel(a, b, c):
    try:
        i = a.split(':')
        j = b.split(":")
        k = c.split(':')
        m = list(k)
        lat1, long1 = radians(float(i[2])), radians(float(i[3]))
        lat2, long2 = radians(float(j[2])), radians(float(j[3]))
    except IndexError and ValueError and TypeError and AttributeError:
        print("Please input proper Values !!")
    else:
        r = 6370.0

        dlon = long2 - long1
        dlat = lat2 - lat1

        l = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        k = 2 * atan2(sqrt(l), sqrt(1 - l))

        distance = round((r * k) / 1.609344)
        m.append(str(distance))
        d = ":".join(m[1:])

        print(d)


travel({'d': 'u'}, ('LOC:NYC:40.7127:-74.0059'), ['TRIP:COFFEE1C:CHI:NYC'])


def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i

        else:
            return [h[n], i]
        print(h)

print(twoSum([56, 48, 92, 52], 100))


def findTriplets(arr):
    lst = []
    ss = set()
    for i in range(len(arr)-1):
        s = set()

        for j in range(i+1, len(arr)):
            x = -(arr[i]+arr[j])
            if x in s:
                lst.append([x, arr[i], arr[j]])
            else:
                s.add(arr[j])
    seen = set()
    a = [x for x in lst if frozenset(x) not in seen and not seen.add(frozenset(x))]
    return a
print(findTriplets([0, -1, 2, -3, 1]))

def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        l, h = i + 1, len(nums) - 1
        while l < h:
            sum = nums[i] + nums[l] + nums[h]
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                l += 1
            else:
                h -= 1
        if diff == 0:
            break
    return target - diff
print(threeSumClosest([-1, 2, 1, -4], 1))


from collections import Counter

def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    if not arr1:
        return []
    elif not arr2:
        return sorted(arr1)
    cnt1 = collections.Counter(arr1)
    ret = []

    for key in arr2:
        ret += ([key] * cnt1[key])
        del cnt1[key]

    cnt1_list = sorted(cnt1.items())
    for num, i in cnt1_list:
        ret += ([num] * i)

    return ret

def flipAndInvertImage(A):
    ls = []
    for i in A:
        i = i[::-1]
        ls.append(i)
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][j] == 0:
                ls[i][j] = 1
            else:
                ls[i][j] = 0
            j += 1
        i += 1
    return ls

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

root1 = [3, 5, 1, 6, 2, 9, 8, 'null', 'null', 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, 'null', 'null', 'null', 'null', 'null', 'null', 9, 8]

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.lis1,self.lis2 = [],[]

        if not root1 and not root2:
            return 1
        if not root1 and root2 or (not root2 and root1):
            return 0

        def helper1(root):
            if not root:
                return

            if not root.left and not root.right:
                self.lis1.append(root.val)


            if root.left:
                helper1(root.left)
            helper1(root.right)
        def helper2(root):
            if not root:
                return

            if not root.left and not root.right:
                self.lis2.append(root.val)


            if root.left:
                helper2(root.left)
            helper2(root.right)

        helper1(root1)
        helper2(root2)

        return self.lis1==self.lis2

result = []


def isPalindrome(st):  # checking of string if it is palindrome or not
    if st == st[::-1]:
        return True
    return False


def palindromePartition(temp, string):
    if len(string) is 0:  # base case
        result.append(temp)  # appending the partitioned palindromes
        return

    for i in range(1, len(string) + 1):
        if isPalindrome(string[:i]):
            palindromePartition(temp + [string[:i]], string[i:])


palindromePartition([], 'aab')
print(result)

def minCostToMoveChips(self, position: List[int]) -> int:
    odd = 0
    even = 0
    for p in position:
        if p % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        return odd
    return even

def maxProfit(prices, fee: int) -> int:
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

print(maxProfit([1,3,2,8,4,9, 9, 5, 7, 9, 3, 65, 89, 9000, 5000], 2))

url = "https://jsonmock.hackerrank.com/api/articles?/author="


def getArticleTitles(author):
    # Write your code here
    headers = {
        'author': author
    }
    r = requests.get(url, headers=headers)

    soup = Beautifulsoup(r.text, 'html.parser')
    l = soup.find('ul', {"class": 'title'})

    for i in l.findAll('title'):
        print(i.text)


getArticleTitles('epage')


import json


# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.

class MarkingPositionMonitor:
    dict_for_inst = {}

    def __init__(self):
        pass

    '''
        dict_for_inst = {
            "symbol" : {
                position : 0, 
                orders: {
                "order_id" : [messages],
                "order_id" : [messages],
                "order_id" : [messages]
                }
            }
        }


        message = {
            "type": "NEW",
            "symbol": "MSFT",
            "order_id": 5,
            "side": "SELL",
            "quantity": 1100,
            "time": "2016-12-22T12:07:04.521073"
        }

        from the question
        {
            "type": "NEW",
            "symbol": "MSFT",
            "order_id": 5,
            "side": "SELL",
            "quantity": 1100,
            "time": "2016-12-22T12:07:04.521073"
        }

        AAPL, IBM, MSFT


        NEW, 				out
        ORDER_ACK,
        ORDER_REJECT
        CANCEL, 			out
        CANCEL_ACK,
        CANCEL_REJECT,
        FILL


        buying - getting
        selling - giving 
        position - shares of instumenet I own
        flat - long - short

        return marking position		
    '''

    def on_event(self, message):
        message = json.loads(message)
        typ = message["type"]
        oid = str(message["order_id"])

        if typ == "NEW":
            sym = message["symbol"]
            if sym not in self.dict_for_inst:
                self.dict_for_inst[sym] = [0, {}]  # position, message list
            syd = message["side"]
            qty = message["quantity"]
            if syd == "SELL":
                self.dict_for_inst[sym][0] -= qty
                if len(self.dict_for_inst[sym][1][oid]) == 0:
                    self.dict_for_inst[sym][1][oid] = [message]
                else:
                    self.dict_for_inst[sym][1][oid].append(message)
            if syd == "BUY":
                if len(self.dict_for_inst[sym][1][oid]) == 0:
                    self.dict_for_inst[sym][1][oid] = [message]
                else:
                    self.dict_for_inst[sym][1][oid].append(message)

        if typ == "ORDER_ACK":
            pass
            # self.dict_for_inst[sym][1][oid].append(message)

        if typ == "ORDER_REJECT":
            if self.dict_for_inst[sym][1][oid][-1]["side"] == "SELL" and self.dict_for_inst[sym][1][oid][-1][
                "order_id"] == oid:
                self.dict_for_inst[sym][0] += self.dict_for_inst[sym][1][oid].pop()["quantity"]
                del (self.dict_for_inst[sym][1][oid])
            if self.dict_for_inst[sym][1][oid][-1]["side"] == "BUY":
                del (self.dict_for_inst[sym][1][oid])

        if typ == "CANCEL":
            self.dict_for_inst[sym][1][oid].append(message)

        if typ == "CANCEL_ACK":
            if self.dict_for_inst[sym][1][oid][-1][
                "type"] == "CANCEL":  # and any[x["type"] == "NEW" for x in self.dict_for_inst[sym][1][oid]]:
                self.dict_for_inst[sym][0] += self.dict_for_inst[sym][1][oid].pop()["quantity"]
                del (self.dict_for_inst[sym][1][oid])

        '''
                dict_for_inst = {
                    "symbol" : [
                        position, {
                        "order_id" : [messages],
                        "order_id" : [messages],
                        "order_id" : [messages]
                        }
                    ]
                }
                message = {
                    "type": "NEW",
                    "symbol": "MSFT",
                    "order_id": 5,
                    "side": "SELL",
                    "quantity": 1100,
                    "time": "2016-12-22T12:07:04.521073"
                }
        '''

        if typ == "FILL":
            for y in range(len(self.dict_for_inst)):
                for x in self.dict_for_inst[sym][1]:
                    if self.dict_for_inst[sym][1][x][-1]["side"] == "BUY":
                        self.dict_for_inst[sym][0] += int(self.dict_for_inst[sym][1][x][-1]["quantity"])
        return self.dict_for_inst[sym][0]


a = MarkingPositionMonitor()
m = """{"type": "NEW", "symbol": "AAPL", "order_id": 1, "side": "BUY", "quantity": 1700, 
"time": "2017-03-15T10:15:20.178562"} """
a.on_event(m)

def airportGates2(arr, dep):
    dep = sorted(dep)
    currentPlanes = 1
    currentDeparturePosition = 0
    maxArrival = 1

    for i in range(len(arr)):
        arrTime = arr[i]
        maxArrival = max(maxArrival, currentPlanes)
        currentPlanes += 1

        for j in range(currentDeparturePosition, len(dep)):
            if dep[j] < arrTime:
                currentDeparturePosition = j
                currentPlanes -= 1
            else:
                break

    return maxArrival

print(airportGates2([630, 645, 730, 1100], [700, 845, 1015, 1130]))

def roman_number(number):
    roman_char = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV', 1: 'I'}
    out = ''
    for val, c in roman_char.items():
        if number & val:
            continue
        repeat, number = divmod(number, val)
        out += repeat * c
    return out

def almostIncreasingSequence(sequence):
    c0,c1=1,1
    n=len(sequence)
    l1=[]
    l2=[]
    for i in sequence:
        l1.append(i)
        l2.append(i)
    for i in range(1,n):
        if sequence[i-1]>=sequence[i]:
            del l1[i]
            del l2[i-1]
            break
    for i in range(1,n-1):
        if l1[i-1]>=l1[i]:
            c0=0
            break
    for i in range(1,n-1):
        if l2[i-1]>=l2[i]:
            c1=0
            break
    return bool(c0 or c1)

print(almostIncreasingSequence([1, 3, 2, 1]))


import collections

# Throttling gateway sol'n @Citadel

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
