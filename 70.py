import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        f = np.zeros((n+1), dtype=int)
        f[0] = 1
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

if __name__ == "__main__":
    n = 4
    r = Solution().climbStairs(n)
    print(r)