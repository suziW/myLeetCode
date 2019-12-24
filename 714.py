# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/
from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        dpi0, dpi1 = 0, float('-inf')
        for i in range(len(prices)):
            dpi0, dpi1 = max(dpi0, dpi1 + prices[i]), max(dpi1, dpi0 - prices[i] - fee)
        return dpi0


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    r = Solution().maxProfit(prices, fee)
    print(r)