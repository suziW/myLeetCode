import numpy as np
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = np.zeros(len(nums), dtype=int)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

if __name__ == "__main__":
    l = [1,3,1]
    r, dp = Solution().rob(l)
    print(r)
    print(dp)