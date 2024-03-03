from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i+1


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 5, 6, 6, 7]
    r = Solution().removeDuplicates(nums)
    print(r)