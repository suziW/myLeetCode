class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + right + 1 >>1
            # if mid**2 == x:
            #     return mid
            if mid**2 > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == "__main__":
    x = 9
    r = Solution().mySqrt(x)
    print(r)