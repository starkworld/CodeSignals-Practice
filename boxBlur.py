"""Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You
can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm distorts the input image in the following
way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3
square that has its center at x, including x itself. All the pixels on the border of x are then removed. Return the
blurred image as an integer, with the fractions rounded down.
"""
import math
import numpy as np
import skimage.measure


def boxBlur(image):
    result = []
    row = len(image)
    col = len(image[0])

    for i in range(1, row - 1):
        value = []
        for j in range(1, col - 1):
            pixel = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    pixel += image[x][y]
            value.append(pixel // 9)
        result.append(value)

    return result

    # a = np.array(image)
    # b = skimage.measure.block_reduce(a, (3, 3), np.mean(a, dtype=np.int64))
    # return b


print(boxBlur([[7, 4, 0, 1],
               [5, 6, 2, 2],
               [6, 10, 7, 8],
               [1, 4, 2, 0]]))
