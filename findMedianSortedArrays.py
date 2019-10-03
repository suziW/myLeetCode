# 自己想的算法，感觉吊打一切，时间复杂度log(min(m, n))。
# 主要思路是比较两个数组中位数，切掉中位数较小数组左边一部分，切掉中位数较大数组右边一部分，切掉长度为长度较小数组长度一半减去1，为了不切到算中位数的数。
#一直到其中一个数组切到长度等于2，这时候可以将另一个数组左右两边切掉一样的长度，切完后总长度为3或4
#最后简单暴力合并两个短数组排序求中位数了
import math
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        print('--------------------------------------------')
        print(nums1)
        print(nums2)

        if nums1 == []:
            print('in s1 none')
            return findMedian(nums2)
        if nums2 == []:
            print('in s2 none', findMedian(nums1))
            return findMedian(nums1)
        if len(nums1) <= 2:
            if len(nums2) > 4:
                cut = math.ceil(len(nums2) / 2) - 2
                nums2 = nums2[cut, -cut]
            nums = nums1 + nums2
            nums.sort()
            return findMedian(nums)
        if len(nums2) <= 2:
            if len(nums1) > 4:
                cut = math.ceil(len(nums1) / 2) - 2
                nums1 = nums1[cut, -cut]
            nums = nums1 + nums2
            nums.sort()
            return findMedian(nums)

        median1 = findMedian(nums1)
        median2 = findMedian(nums2)
        smallLen = math.ceil(min(len(nums1), len(nums2)) / 2) - 1

        # if median1 == median2:
        #     return median1

        print(median1)
        print(median2)
        print(smallLen)
        if median1 < median2:
            return Solution().findMedianSortedArrays(nums1[smallLen:],
                                                     nums2[:-smallLen])
        else:
            return Solution().findMedianSortedArrays(nums1[:-smallLen],
                                                     nums2[smallLen:])


def findMedian(l: List[int]) -> float:
    print('>>>>>>', l)
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]


if __name__ == "__main__":
    s1 = Solution().findMedianSortedArrays([1, 2, 3], [1, 2, 2])
    print('result is ', s1)