class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[1] = 1
        l2 = 1
        l3 = 1
        l5 = 1
        for i in range(2, n+ 1):
            print(l2, l3, l5)
            dp[i] = min(dp[l2]*2, dp[l3]*3, dp[l5]*5)
            if dp[i] >= 2 * dp[l2]:
                l2 += 1
            if dp[i] >= 3* dp[l3]:
                l3 += 1
            if dp[i] >= 5*dp[l5]:
                l5+= 1
        print(dp)
        return dp[n]

if __name__ == "__main__":
    n = 11
    r = Solution().nthUglyNumber(n)
    print(r)