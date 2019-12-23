from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i-j], dp[i])
            dp[i] += 1
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == "__main__":
    coins = [2]
    amount = 11
    r = Solution().coinChange(coins, amount)
    print(r)