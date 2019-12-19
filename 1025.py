import numpy as np
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = np.zeros(N+1, dtype=bool)
        for i in range(2, N+1):
            for j in range(1, i): # 选择的数
                if i % j == 0 and dp[i -j] == False:
                    dp[i] = True
                    break
            print(i, dp[i])
        return dp[-1], dp

if __name__ == "__main__":
    N = 7
    r, dp = Solution().divisorGame(N)
    print(r)
    print(dp)
