from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i, num in enumerate(nums):
            while stack != [] and num > nums[stack[-1]]:
                res[stack.pop()] = num
            stack.append(i)
        print(stack)
        print(res)
        for i, num in enumerate(nums):
            while stack != [] and num > nums[stack[-1]]:
                res[stack.pop()] = num
            if i == stack[0]:
                while stack != []:
                    res[stack.pop()] = -1
                break
        print(stack)
        print(res)
        return res
if __name__ == "__main__":
    nums = [1,1,1,1,1]
    r = Solution().nextGreaterElements(nums)
    print(r)