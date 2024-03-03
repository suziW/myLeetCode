from typing import List


def gridPrint(grid):
    for row in range(len(grid)):
        print(grid[row])


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        num = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    num += 1
        return num

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        m = len(grid)
        n = len(grid[0])
        for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ii = i + direction[0]
            jj = j + direction[1]
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                self.dfs(grid, ii, jj)


if __name__ == "__main__":
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    gridPrint(grid)
    r = Solution().numIslands(grid)
    print(r)
