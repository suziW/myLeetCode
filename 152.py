from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_= float('-inf')
        max_num = 1
        min_num = 1
        for n in nums:
            if n < 0:
                max_num, min_num = min_num, max_num
            max_num = max(max_num*n, n)
            min_num = min(min_num*n, n)
            max_ = max(max_num, max_)
            print(max_num, min_num, max_)
        return max_    

if __name__ == "__main__":
    l = [2, 3, -2, 4]
    r = Solution().maxProduct(l)
    print(r)