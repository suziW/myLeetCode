from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l < r:
            m = l + r >> 1
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 13
    r = Solution().search(nums, target)
    print(r)