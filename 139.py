from typing import List
import re
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True
        # dp[0] = s[0] in wordDict
        for i in range(len(s)):
            for j in range(i+1):
                dp[i] = dp[j-1] and s[j:i+1] in wordDict
                if dp[i]: break                                    
            print(i, dp)
        return dp[-2]

if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    r = Solution().wordBreak(s, wordDict)
    print(r)