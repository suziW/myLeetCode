from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            m = l + r >> 1
            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                r = m
        print(r)
        return letters[l] if l < len(letters) else letters[0]

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = 'j'
    r = Solution().nextGreatestLetter(letters, target)
    print(r)