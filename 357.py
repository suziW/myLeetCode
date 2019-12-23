class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        muls = 9
        for i in range(1, n+1):
            dp[i] = dp[i-1] + muls
            muls *= max(10 - i, 0)
        print(dp)
        return dp[-1]

if __name__ == "__main__":
    n = 9
    r = Solution().countNumbersWithUniqueDigits(n)
    print(r)