from typing import List
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]

        p = (left + right) // 2
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p+1, right)
        cross_sum = self.cross(nums, left, p, right)

        return max(left_sum, right_sum, cross_sum)

    def cross(self, nums, left, p, right):
        left_subsum = -np.inf
        curr_sum = 0
        for i in range(p, left-1, -1):
            curr_sum += nums[i]
            left_subsum = max(curr_sum, left_subsum)
        
        right_subsum = -np.inf
        curr_sum = 0
        for i in range(p + 1, right+1):
            curr_sum += nums[i]
            right_subsum = max(curr_sum, right_subsum)
        return left_subsum + right_subsum

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        c = []
        m = []
        curr_sum = max_sum = nums[0]
        c.append(curr_sum)
        m.append(max_sum)
        print('---')

        for i in range(1, n):
            # if curr_sum < 0:
            #     curr_sum = nums[i]
            # else:
            #     curr_sum += nums[i]
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(curr_sum, max_sum)
            print('----')
            c.append(curr_sum)
            m.append(max_sum)
        return max_sum, m, c


if __name__ == "__main__":
    l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    z = np.zeros(9)
    r, m, c = Solution().maxSubArray(l)
    print(r)
    print(m)
    print(c)

    plt.figure()
    plt.plot(z)
    plt.plot(l, '-r')
    plt.title('l')
    # plt.figure()
    plt.plot(m, '-b')
    plt.title('m')
    # plt.figure()
    plt.plot(c, '-y')
    plt.title('c')
    plt.show()