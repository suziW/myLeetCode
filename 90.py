from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []


        def backtrack(l: List[int], index: int):
            result.append(l[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:  #我们要对同一树层使用过的元素进行跳过
                    continue
                l.append(nums[i])
                backtrack(l, i+1)
                l.pop()
        
        backtrack([], 0)
        return result


if __name__ == '__main__':
    nums = [2, 1, 2]
    r = Solution().subsetsWithDup(nums)
    print(r)
