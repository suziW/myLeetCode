import numpy as np


def maxHeight(wallPositions, wallHeights):
    # Write your code here

    def maxh(i):
        left = wallPositions[i]
        right = wallPositions[i + 1]
        leftH = wallHeights[i]
        rightH = wallHeights[i + 1]
        while left < right - 1:
            if leftH < rightH:
                left += 1
                leftH += 1
            else:
                right -= 1
                rightH += 1
        print(left, right, leftH, rightH)
        return max(leftH, rightH)

    maxHeight_ = 0
    for i in range(len(wallPositions) - 1):
        if wallPositions[i + 1] - wallPositions[i] > 1:
            return 0
            maxHeight_ = max(maxHeight_, maxh(i))
    return maxHeight_


if __name__ == "__main__":
    wallPositions = [1, 3, 7]
    wallHeights = [4, 3, 3]
    r = maxHeight(wallPositions, wallHeights)
    print(r)