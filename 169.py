from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > len(nums)/2:
                return num

if __name__ == "__main__":
    nums = [3, 2, 3]
    r = Solution().majorityElement(nums)
    print(r)