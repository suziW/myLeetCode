from typing import List


class Solution:

    def __init__(self):
        self.area = 0

    def update(self, a):
        self.area = self.area if self.area >= a else a

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        while (r > l):
            print('============================')
            print(l, r, height[l], height[r])
            self.update((r - l) * min(height[r], height[l]))

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return self.area


if __name__ == "__main__":
    height = [2, 3, 4, 5, 18, 17, 6]
    r = Solution().maxArea(height)
    print(r)