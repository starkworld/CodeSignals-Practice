def matrixElementsSum(matrix):
    summ = 0
    for i in range(0, len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] > 0:
                summ += matrix[j][i]
                j += 1
            else:
                break
        i += 1
    return summ
