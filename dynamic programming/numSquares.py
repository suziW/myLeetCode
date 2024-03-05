class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        return dp[-1]


if __name__ == "__main__":
    n = 12
    r = Solution().numSquares(n)
    print(r)
