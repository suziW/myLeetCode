import numpy as np
from typing import List


class Solution:
    def quickSort(self, nums: List[int]):
        self.nums = nums
        self.sort(0, len(nums) - 1)

    def kLarge(self, nums: List[int], k: int) -> int:
        self.k = len(nums) - k
        self.nums = nums
        return self._kLarge(0, len(nums) - 1)

    def _kLarge(self, l: int, r: int) -> int:
        p = self.partition(l, r)
        if p < self.k:
            return self._kLarge(p + 1, r)
        elif p == self.k:
            return self.nums[p]
        else:
            return self._kLarge(l, p - 1)

    def sort(self, l: int, r: int):
        if l < r:
            p = self.partition(l, r)
            self.sort(l, p-1)
            self.sort(p+1, r)

    def partition(self, l: int, r: int) -> int:
        index = l
        for i in range(l, r):
            if self.nums[i] < self.nums[r]:
                self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
                index += 1
        self.nums[r], self.nums[index] = self.nums[index], self.nums[r]
        return index


if __name__ == "__main__":
    # l = np.random.randint(0, 100, 9)
    l = [62, 9, 94, 5, 96, 55, 67, 20, 0, 4, 86, 55, 83, 71, 84, 25, 95, 68]
    print(l)
    Solution().quickSort(l)
    print('result is:', l)
    print('2Large is {}'.format(Solution().kLarge(l, 2)))
    print('4Large is {}'.format(Solution().kLarge(l, 4)))
