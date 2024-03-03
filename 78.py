from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        def backtrack(combination, index):
            r.append(combination[:])
            for i in range(index, len(nums)):
                combination.append(nums[i])
                backtrack(combination, i + 1)
                combination.pop()
        backtrack([], 0)
        return r

if __name__ == "__main__":
    nums = [1, 2, 3]
    r = Solution().subsets(nums)
    print(r)