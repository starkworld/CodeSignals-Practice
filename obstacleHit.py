"""
You are given an array of integers representing coordinates of obstacles situated on a straight line. Assume that
you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length
represented by some integer. Find the minimal length of the jump enough to avoid all the obstacles.
"""
from typing import List


def avoidObstacles(inputArray: List[int]) -> int:
    obstcle: List[int] = sorted(inputArray)

    jumps: int = 1

    obstacle_hit: bool = True

    while obstacle_hit:

        obstacle_hit: bool = False
        jumps += 1

        for i in range(0, len(inputArray)):
            if obstcle[i] % jumps == 0:
                obstacle_hit: bool = True
                break

    return jumps
