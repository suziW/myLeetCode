import numpy as np
from typing import List


class Solution:
    def quickSort(self, l: List[int]):
        self.sort(l, 0, len(l) - 1)

    def sort(self, l: List[int], left: int, right: int):
        if left >= right:
            return

        low, high = left, right
        pivot = left
        while right > left:
            while l[right] > l[pivot] and right > left:
                right -= 1
            while l[left] <= l[pivot] and right > left:
                left += 1
            l[left], l[right] = l[right], l[left]
        l[pivot], l[left] = l[left], l[pivot]
        self.sort(l, low, left - 1)
        self.sort(l, left + 1, high)


if __name__ == "__main__":
    l = np.random.randint(0, 100, 20)
    # l = [62, 9, 94, 5, 96, 55, 67, 20, 0, 4, 86, 55, 83, 71, 84, 25, 95, 68]
    print(l)
    Solution().quickSort(l)
    print('result is:', l)
