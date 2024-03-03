# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dpi00, dpi01 = 0, float('-inf')
        dpi10, dpi11 = 0, float('-inf')
        for i in range(len(prices)):
            dpi10, dpi11 = max(dpi10, dpi11 + prices[i]), max(dpi11, dpi00 - prices[i])
            dpi00, dpi01 = max(dpi00, dpi01 + prices[i]), max(dpi01, -prices[i])
        return dpi10


if __name__ == "__main__":
    p = [3, 3, 5, 0, 0, 3, 1, 4]
    r = Solution().maxProfit(p)
    print(r)