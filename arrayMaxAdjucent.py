"""Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3"""


def arrayMaximalAdjacentDifference(inputArray):
    max = 0
    long = len(inputArray)

    for i in range(1, long - 1):

        if abs(inputArray[i] - inputArray[i - 1]) > max:
            max = abs(inputArray[i] - inputArray[i - 1])
        if abs(inputArray[i] - inputArray[i + 1]) > max:
            max = abs(inputArray[i] - inputArray[i + 1])

    return max