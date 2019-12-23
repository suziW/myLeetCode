from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            print('left:', left, 'right:', right)
        return left


if __name__ == "__main__":
    nums = [1, 3, 5 , 6]
    target = 5
    r = Solution().searchInsert(nums, target)
    print(r)