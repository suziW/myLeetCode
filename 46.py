from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        def backtrack(l, nums):
            print(l, nums)
            if len(nums) == 0:
                r.append(l[:])
            for i in range(len(nums)):
                l.append(nums.pop(i))
                backtrack(l, nums)
                nums.insert(i,l.pop())
        backtrack([], nums)
        return r

if __name__ == "__main__":
    nums = [1,2,3]
    r = Solution().permute(nums)
    print(r)