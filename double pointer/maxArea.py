from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    r = Solution().maxArea(height)
    print(r)