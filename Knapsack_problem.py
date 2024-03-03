class Solution:
    def ksnap(self, w, items):
        dp = [0 for _ in range(w+1)]
        print(dp)

        for i in range(len(items)):
            weight, value = items[i]
            for k in range(w, 0, -1):   # 正序即是完全背包问题
                if k - weight < 0:
                    dp[k] = dp[k]
                else:
                    dp[k] = max(dp[k], dp[k-weight] + value)
            print('================================', items[i])
            print(dp)


if __name__ == "__main__":
    items = [(5, 12), (4, 3), (7, 10), (2, 3), (6, 6)]
    w = 15
    r = Solution().ksnap(w, items)
    print(r)