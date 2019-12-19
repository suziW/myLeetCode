from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [float('inf') for _ in range(len(triangle)+1)]
        dp[0] = 0
        for i in range(len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                dp[j] = triangle[i][j] + min(dp[j-1], dp[j])
            print(dp)
        return min(dp)
        
        
if __name__ == "__main__":
    tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
    r = Solution().minimumTotal(tri)
    print(r)