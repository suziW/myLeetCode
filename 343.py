class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(max(i-j, dp[i-j]) * j, dp[i])
        print(dp)
        return dp[-1]

if __name__ == "__main__":
    n = 10
    r = Solution().integerBreak(n)
    print(r)