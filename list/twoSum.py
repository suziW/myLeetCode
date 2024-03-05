from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return d[target - n], i
            d[n] = i




if __name__ == "__main__":
    numbers = [5, 25, 75]
    target = 100
    r = Solution().twoSum(numbers, target)
    print(r)