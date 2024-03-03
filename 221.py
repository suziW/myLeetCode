from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []: return 0
        dp = [0 for _ in range(len(matrix[0])+1)]
        preCorner, max_ = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp = dp[j]
                if matrix[i][j] == '1':
                    # print(dp[j])
                    dp[j] = min(dp[j-1], dp[j], preCorner) + 1
                    max_ = max(max_, dp[j])
                else:
                    dp[j] = 0
                preCorner = temp
            print(dp)
        return max_ * max_


if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]

    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    r = Solution().maximalSquare(matrix)
    print(r)