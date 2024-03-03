import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = np.zeros((len(s), len(s)))
        longest = 1
        for d in range(0, len(s)):
            for i in range(0, len(s) - d):
                if d == 0:
                    dp[i, i+d] = 1
                elif d == 1:
                    if s[i] == s[i+d]:
                        dp[i, i+d] = 1
                elif dp[i+1, i+d-1] and s[i] == s[i+d]:
                    dp[i, i+d] = 1
                    
                if dp[i, i+d] == 1:
                    longest = max(longest, d+1)
        print(dp)
        return longest

if __name__ == '__main__':
    s = 'bb'
    r = Solution().longestPalindrome(s)
    print(r)
