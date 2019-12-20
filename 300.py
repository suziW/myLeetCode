from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+1)]
        # dp[0] = 1
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j], dp[i])
            dp[i] += 1
        print(dp)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            i, j = 0, len(tail)
            while i < j:
                m = (i + j) // 2
                if tail[m] < num:
                    i = m + 1
                else:
                    j = m
            if j == len(tail):
                tail.append(num)
            else:
                tail[j] = num
            print(i, j)
            print(tail)
        return len(tail)


if __name__ == "__main__":
    l = [1,3,6,7,9,4,10,5,6]
    r = Solution().lengthOfLIS(l)
    print(r)
