import numpy as np
from typing import List


class Solution:
    def mergeSort(self, nums: List[int]):
        self.nums = nums
        self.sort(0, len(nums) - 1)

    def sort(self, l: int, r: int):
        if l < r:
            m = (l + r) // 2
            self.sort(l, m)
            self.sort(m+1, r)
            self.merge(l, r)

    def merge(self, l, r):
        m = (l + r) // 2
        l_nums = self.nums[l: m+1]
        r_nums = self.nums[m+1: r+1]
        index = l
        l_index = 0
        r_index = 0
        while True:
            if l_nums[l_index] < r_nums[r_index]:
                self.nums[index] = l_nums[l_index]
                l_index += 1
            else:
                self.nums[index] = r_nums[r_index]
                r_index += 1
            index += 1

            if l_index == len(l_nums):
                while r_index < len(r_nums):
                    self.nums[index] = r_nums[r_index]
                    r_index += 1
                    index += 1
                break

            if r_index == len(r_nums):
                while l_index < len(l_nums):
                    self.nums[index] = l_nums[l_index]
                    l_index += 1
                    index += 1
                break


if __name__ == "__main__":
    l = list(np.random.randint(0, 99, 9))
    # print(type(l))
    # l = [62, 9, 94, 5, 96, 55, 67, 20, 0, 4, 86, 55, 83, 71, 84, 25, 95, 68]
    print(l)
    Solution().mergeSort(l)
    print('result is:', l)
