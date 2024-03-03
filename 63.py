from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0 for _ in range(len(obstacleGrid[0])+1)]
        dp[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                    dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j-1]
            # print(dp)
        return dp[-2]

if __name__ == "__main__":
    grid = [[0,1]]
    r=Solution().uniquePathsWithObstacles(grid)
    print(r)