import numpy as np


class Solution:
    def climbStairs(self, n: int) -> int:
        n_1, n_2 = 2, 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            n_1, n_2 = n_1+n_2, n_1
        return n_1


if __name__ == "__main__":
    n = 4
    r = Solution().climbStairs(n)
    print(r)
