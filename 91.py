class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[-1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-2] == '2' and s[i]>='1' and s[i]<='6'):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-2]


if __name__ == "__main__":
    s = '226'
    print(s[-1:1])
    r = Solution().numDecodings(s)
    print(r)