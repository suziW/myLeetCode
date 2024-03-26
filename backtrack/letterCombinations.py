from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digits2letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mon",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        r = []

        def backtrack(s, index):
            if index == len(digits):
                r.append(s)
                return
            for c in digits2letters[digits[index]]:
                backtrack(s + c, index + 1)

        backtrack("", 0)
        return r


if __name__ == "__main__":
    s = "23"
    r = Solution().letterCombinations(s)
    print(r)
