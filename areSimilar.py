"""Two arrays are called similar if one can be obtained
 from another by swapping at most one pair of elements
 in one of the arrays"""


def areSimilar(a, b):
    return sorted(a) == sorted(b) and sum([x != y for x, y in zip(a, b)]) <= 2


print(
    areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]))
