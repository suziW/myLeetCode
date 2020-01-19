from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return
            if board[i][j] == 'O':
                board[i][j] = 'Y'
                helper(i-1, j)
                helper(i+1, j)
                helper(i, j-1)
                helper(i, j+1)
                
        for i in range(len(board)):
            helper(i, 0)
            helper(i, len(board[0])-1)
        for j in range(len(board[0])):
            helper(0, j)
            helper(len(board)-1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'Y': board[i][j] = 'O'

if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(board)
    Solution().solve(board)
    print(board)