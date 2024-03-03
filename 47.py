from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        def backtrack(combination, nums):
            if nums == []:
                r.append(combination)
            temp = float('inf')
            for i in range(len(nums)):
                if nums[i] == temp:
                    continue
                backtrack(combination + [nums[i]], nums[:i] + nums[i+1:])
                temp = nums[i]
        backtrack([], nums)
        return r
                

if __name__ == "__main__":
    nums = [-1,2,-1,2,1,-1,2,1]
    r = Solution().permuteUnique(nums)
    print(r)        