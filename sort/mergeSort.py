import numpy as np
from typing import List


def mergeSort(nums: List[int]):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    mergeSort(left)
    mergeSort(right)

    # merge left and right
    l, r, n = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            nums[n] = left[l]
            l += 1
        else:
            nums[n] = right[r]
            r += 1
        n += 1
    while l < len(left):
        nums[n] = left[l]
        l += 1
    while r < len(right):
        nums[n] = right[r]
        r += 1

    return nums


if __name__ == "__main__":
    l = list(np.random.randint(0, 99, 9))
    print(l)
    mergeSort(l)
    print("result is:", l)
