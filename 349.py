from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for n in nums1:
            if not dic.get(n):
                dic[n] = 1
            else:
                dic[n] += 1
        l = []
        for n in nums2:
            if dic.get(n):
                dic[n] -= 1
                l.append(n)
        return l

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    r = Solution().intersection(nums1, nums2)
    print(r)