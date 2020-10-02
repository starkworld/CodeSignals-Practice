import heapq
from typing import List


def findMaximizedCapital(k: int, W: int, P: List[int], C: List[int]) -> int:
    if W > max(C):
        return W + sum(heapq.nlargest(k, P))

    minH = [[C[x], x] for x in range(len(C))]
    maxH = []
    heapq.heapify(minH)
    while k:
        while minH and minH[0][0] <= W:
            _, idx = heapq.heappop(minH)
            heapq.heappush(maxH, -P[idx])

        if not maxH:
            break

        W += -heapq.heappop(maxH)
        k -= 1

    return W
