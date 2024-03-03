class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        r = 1.0
        p = x
        while n > 0:
            if n % 2 == 1:
                r *= p
            p *= p
            n = n >> 1
        return r

if __name__ == "__main__":
    x = 2
    n = -2
    r = Solution().myPow(x, n)
    print(r)