class Solution:
    def climbStairs(self, n: int) -> int:
        # T(n) = T(n-1) + T(n-2)
        # T(1) = 1
        # T(2) = 2
        if n == 1: return 1
        if n == 2: return 2
        t = [0] * (n + 1)
        t[1] = 1
        t[2] = 2
        for i in range(3, n + 1):
            t[i] = t[i - 1] + t[i - 2]
        return t[n]


if __name__ == "__main__":
    n = 3
    r = Solution().climbStairs(n)
    print(r)