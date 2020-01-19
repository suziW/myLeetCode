def gridPrint(grid):
    for row in range(len(grid)):
        print(grid[row])

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[]: return 0```

        raw = len(grid)
        column = len(grid[0])
        def helper(i, j, count):
            if i < 0 or i >= raw or j < 0 or j >= column: return
            if grid[i][j] == '1':
                grid[i][j] = count
                helper(i-1, j, count)
                helper(i+1, j, count)
                helper(i, j-1, count)
                helper(i, j+1, count)

        count = 0
        for i in range(raw):
            for j in range(column):
                if grid[i][j] == '1': count += 1
                helper(i, j, count)
        gridPrint(grid)
        return count

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    gridPrint(grid)
    r = Solution().numIslands(grid)
    print(r)