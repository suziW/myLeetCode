# 哈希表

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            if (target - num) in hashmap:
                return [i,hashmap[target - num]]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

if __name__ == "__main__":
    print(Solution().twoSum([1, 2, 4, 6], 6))
    pass