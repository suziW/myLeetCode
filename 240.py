class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        def search(s, e):
            if s[0] < e[0] and s[1] < e[1]:
                m = [s[0] + e[0] >> 1, s[1] + e[1] >> 1]
                if matrix[s[0]][s[1]] >= target and matrix[m[0]][m[1]] <= target:
                    search(s, m)
                if 
            else:
                return s, e

if __name__ == "__main__":
    matrix = [[1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
    target = 5
    r = Solution().searchMatrix(matrix, target)
    print(r)