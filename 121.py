from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        maxP= 0
        for i, j in enumerate(prices):
            if j < prices[b]:
                b = i
            else:
                maxP = max(maxP,j - prices[b])
        return maxP

if __name__ == "__main__":
    l = [7,1,5,3,6,4]
    r = Solution().maxProfit(l)
    print(r)