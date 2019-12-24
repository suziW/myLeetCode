class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l < r:
            m = l + r >> 1
            if m**2 < num:
                l = m + 1
            else:
                r = m
        return l**2 == num

if __name__ == "__main__":
    num = 16
    r = Solution().isPerfectSquare(num)
    print(r)        