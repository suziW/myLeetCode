import numpy as np
from typing import List


class Solution:
    def heapSort(self, nums: List[int]):
        self.nums = nums
        self.buildmaxheap()
        heapsize = len(nums)
        for i in range(len(nums)):
            self.nums[0], self.nums[heapsize - 1] = self.nums[heapsize - 1], self.nums[0]
            heapsize -= 1
            self.heapfy(0, heapsize)

    def kLarge(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.buildmaxheap()

        heapsize = len(nums)
        for i in range(k-1):
            self.nums[0], self.nums[heapsize - 1] = self.nums[heapsize - 1], self.nums[0]
            heapsize -= 1
            self.heapfy(0, heapsize)

        return self.nums[0]

    def heapfy(self, i, heapsize):
        lc = i * 2 + 1 # left child
        rc = i * 2 + 2 # right child
        maxi = i
        if lc < heapsize and self.nums[lc] > self.nums[maxi]:
            maxi = lc
        if rc < heapsize and self.nums[rc] > self.nums[maxi]:
            maxi = rc

        if maxi != i:
            self.nums[i], self.nums[maxi] = self.nums[maxi], self.nums[i]
            self.heapfy(maxi, heapsize)

    def buildmaxheap(self):
        for i in range(len(self.nums) // 2, -1, -1):
            self.heapfy(i, len(self.nums))


if __name__ == '__main__':
    l = list(np.random.randint(0, 99, 9))
    print(l)
    Solution().heapSort(l)
    print(l)

    print(Solution().kLarge(l, 2))