from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # T(n) = max(T(n - 1), T(n - 2) + nums[n])
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    r = Solution().rob(nums)
    print(r)
