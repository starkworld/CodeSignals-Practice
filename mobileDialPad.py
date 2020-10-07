from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        replacements = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        letters = map(lambda x: replacements[x], digits)
        return [''.join(word) for word in product(*letters)]

c = Solution()
print(c.letterCombinations('23'))