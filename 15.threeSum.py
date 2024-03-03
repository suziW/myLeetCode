from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return res

        anchor = 0
        while nums[anchor] <= 0 and anchor < len(nums) - 2:
            left, right = anchor + 1, len(nums) - 1
            while left < right:
                s = nums[anchor] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s == 0:
                    res.append([nums[anchor], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            anchor += 1
            while anchor < len(nums) - 2 and nums[anchor] == nums[anchor - 1]:
                anchor += 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    r = Solution().threeSum(nums)
    print(r)