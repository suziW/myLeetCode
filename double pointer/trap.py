from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        s = 0

        while l < r:
            height_current = min(height[l], height[r])
            while l < r and height[l] <= height_current:
                l += 1
                s += max(0, height_current - height[l])

            height_current = min(height[l], height[r])
            while l < r and height[r] <= height_current:
                r -= 1
                s += max(0, height_current - height[r])

        return s


if __name__ == "__main__":
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4,2,0,3,2,5]
    r = Solution().trap(height)
    print(r)
