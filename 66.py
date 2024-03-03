from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        while i < len(digits):
            if digits[-i] + 1 == 10:
                digits[-i] = 0
                i += 1
            else:
                digits[-i] += 1
                break
        if i == len(digits):
            digits = [1] + digits
        return digits
            

if __name__ == "__main__":
    digits = [1, 2, 3]
    r = Solution().plusOne(digits)
    print(r)