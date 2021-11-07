from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums: List[int]) -> int:
        r, nr = 0, 0
        for n in nums:
            r, nr = max(r, nr + n), max(r, nr)
        return max(r, nr)


if __name__ == "__main__":
    n = [1, 2, 3, 1]
    r = Solution().rob(n)
    print(r)
