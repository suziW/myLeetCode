# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        maxP = 0
        for i, j in enumerate(prices):
            if j < prices[b]:
                b = i
            else:
                maxP = max(maxP, j - prices[b])
        return maxP


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dpi0, dpi1 = 0, float('-inf')
        for i in range(len(prices)):
            dpi0 = max(dpi0, dpi1 + prices[i])
            dpi1 = max(dpi1, -prices[i])
        return dpi0


if __name__ == "__main__":
    l = [7, 1, 5, 3, 6, 4]
    r = Solution().maxProfit(l)
    print(r)