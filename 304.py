from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.sums[i][j] = self.sums[i][j-1] + self.sums[i-1][j]  - self.sums[i-1][j-1] + matrix[i][j]
            print(self.sums[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2][col2] - self.sums[row1-1][col2] - self.sums[row2][col1-1] + self.sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    mat = [[3,0,1,4,2],
           [5,6,3,2,1],
           [1,2,0,1,5],
           [4,1,0,1,7],
           [1,0,3,0,5]]
    r = NumMatrix(mat).sumRegion(2, 1, 4, 3)
    print(r)