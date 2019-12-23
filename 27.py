from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    r = Solution().removeElement(nums, val)
    print(r)