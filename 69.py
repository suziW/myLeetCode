class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + right >>1
            # if mid**2 == x:
            #     return mid
            if mid**2 < x:
                left = mid + 1
            else:
                right = mid
        print(left, right)
        return left -1 if not left**2==x else left


if __name__ == "__main__":
    x = 7
    r = Solution().mySqrt(x)
    print(r)