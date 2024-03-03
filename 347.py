from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        import heapq
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 4, 4, 5]
    k = 2
    r = Solution().topKFrequent(nums, k)
    print(r)