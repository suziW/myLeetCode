from typing import List


class Solution:
    def myLetterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digits2letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mon',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        lengthList = [1]
        for d in digits[::-1]:
            lengthList.append(len(digits2letters[d]) * lengthList[-1])
        lengthList = lengthList[::-1]

        combinations = [''] * lengthList[0]

        for i, d in enumerate(digits):
            for j in range(lengthList[0]):
                combinations[j] += digits2letters[d][j % lengthList[i] //
                                                     lengthList[i + 1]]
            print(combinations)
        return combinations

    def letterCombinations(self, digits):
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


if __name__ == "__main__":
    digits = "323"

    r = Solution().letterCombinations(digits)
    print(r)