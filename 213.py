from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            cur, pre = 0, 0
            for n in nums:
                cur, pre = max(cur, n + pre), cur
            return cur
        return max(rob(nums[1:]), rob(nums[:-1])) if len(nums) != 1 else nums[0]

if __name__ == "__main__":
    n = [1]
    r = Solution().rob(n)
    print(r)