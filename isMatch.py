import numpy as np


class Solution:
    def isMatch(self, text, pattern):
        dp = np.zeros([len(text) + 1, len(pattern) + 1], dtype=np.bool)
        dp[-1, -1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                print('==========', i, j)
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i, j] = dp[i, j + 2] or first_match and dp[i + 1, j]
                else:
                    dp[i, j] = first_match and dp[i + 1, j + 1]
                print(first_match, dp)
        return dp[0, 0]


if __name__ == '__main__':
    s = "ab"
    p = "a*b*"
    print(len(s), len(p))
    r = Solution().isMatch(s, p)
    # print('==>')
    # r = Solution().match('b', ['b'])
    print(r)
