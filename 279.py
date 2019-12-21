# 超出时间限制，没法子
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(int(i**0.5), 0, -1):
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
                if dp[i] in [1, 2]:
                    break
        print(dp)
        return dp[-1]

if __name__ == "__main__":
    n = 51560
    r = Solution().numSquares(n)
    print(r)