import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.zeros([m+1, n+1], dtype = int)
        dp[0, 1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i, j] = dp[i-1, j] + dp[i, j-1]
        return dp[m, n], dp


if __name__ == "__main__":
    m = 7
    n = 3
    r, dp =Solution().uniquePaths(m, n)
    print(r, dp)