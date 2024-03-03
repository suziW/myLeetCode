# 经验：正向遍历不行，试着倒着来啊
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minnums = []
        min_ = nums[0]
        for n in nums:
            min_ = min(min_, n)
            minnums.append(min_)
        print(minnums)

        stack = []
        for i in range(-1, -len(nums)-1):
            if nums[i] > minnums[i]:
                if stack == [] or nums[i] < stack[-1]:
                    stack.append(nums[i])

if __name__ == "__main__":
    nums = [3,5,0,3,4]#[-2,1,1,-2,1,1]
    r = Solution().find132pattern(nums)
    print(r)