"""Given a string, find out if its characters can be rearranged to form a palindrome.
    For inputString = "aabb", the output should be
    palindromeRearranging(inputString) = true.

    We can rearrange "aabb" to make "abba", which is a palindrome."""


def palindromeRearranging(inputString):
    no_of_char = 256
    cnt = [0] * no_of_char
    for i in range(len(inputString)):
        cnt[ord(inputString[i])] = cnt[ord(inputString[i])] + 1

    odd = 0
    for i in range(0, no_of_char):
        if cnt[i] & 1:
            odd = odd + 1
        if odd > 1:
            return False
    return True
