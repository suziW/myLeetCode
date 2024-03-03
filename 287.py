from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    nums = [1,3,4,2,2]
    r = Solution().findDuplicate(nums)
    print(r)