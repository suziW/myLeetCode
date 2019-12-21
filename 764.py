from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur = 0
        pre = 0
        for i in range(len(cost)):
            print(pre, cur,)
            temp = min(pre, cur)  + cost[i]
            pre = cur
            cur = temp
        print(pre, cur)
        return min(cur, pre)


if __name__ == "__main__":
    cost = [0, 1, 1,0]
    r = Solution().minCostClimbingStairs(cost)
    print(r)

