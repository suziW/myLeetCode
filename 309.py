from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dpi0, dpi1 = 0, float('-inf')
        pre = 0
        for i in range(len(prices)):
            dpi0, dpi1, pre = max(dpi0, dpi1 + prices[i]), max(dpi1, pre - prices[i]), dpi0
        return dpi0


if __name__ == "__main__":
    l = [1, 2, 3, 0, 2]
    r = Solution().maxProfit(l)
    print(r)