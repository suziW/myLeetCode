from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [float('inf') for _ in range(len(grid[0])+1)]
        dp[0] = 0
        # dp[-1] = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
            print(dp)
        return dp[-2]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    r=Solution().uniquePathsWithObstacles(grid)
    print(r)