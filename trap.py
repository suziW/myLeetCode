from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        pass

    def differential(self, height: List[int]) -> List[int]:
        diff = []
        diff.append(int(height[0] >= 0))
        for i, _ in enumerate(height[:-1]):
            if height[i + 1] > height[i]:
                diff.append(1)
            elif height[i + 1] < height[i]:
                diff.append(-1)
            else:
                diff.append(0)
            print(i, '=====>', height[i + 1], height[i], diff)
        diff.append(int(0 >= height[-1]))
        return diff


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    r = Solution().differential(height)
    print(r)