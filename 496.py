from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(lambda :-1)
        helper = [float('inf')]
        for i in nums2:
            while i > helper[-1]:
                dic[helper.pop()] = i
            helper.append(i)
        return [dic[i] for i in nums1]

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    r = Solution().nextGreaterElement(nums1, nums2)
    print(r)