from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, i):
            print(r, c, i)
            if i == len(word): return True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if r + dr >= 0 and r + dr < len(board) and c + dc >= 0 and c + dc < len(board[0]) and board[r + dr][c + dc] == word[i]:
                    board[r + dr][c + dc] = ''
                    if backtrack(r + dr, c + dc, i+1):
                        return True
                    board[r + dr][c + dc] = word[i]
                        
            # if r - 1 >= 0 and board[r-1][c] == word[i]: # up
            #     board[r-1][c] = ''
            #     if backtrack(r - 1, c, i+1):
            #         return True 
            #     board[r-1][c] = word[i]

            # if r + 1 < len(board) and board[r+1][c] == word[i]: # down
            #     board[r+1][c] = ''
            #     if backtrack(r + 1, c, i+1):
            #         return True 
            #     board[r+1][c] = word[i]

            # if c - 1 >= 0 and board[r][c-1] == word[i]: # left
            #     board[r][c-1] = ''
            #     if backtrack(r, c-1, i+1):
            #         return True 
            #     board[r][c-1] = word[i]

            # if c + 1 < len(board[0]) and board[r][c + 1] == word[i]: # right
            #     board[r][c + 1] = ''
            #     if backtrack(r, c + 1, i+1):
            #         return True 
            #     board[r][c + 1] = word[i]
                
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    board[r][c] = ''
                    if backtrack(r, c, 1):
                        return True
                    board[r][c] = word[0]
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = 'ABCCED'
    r = Solution().exist(board, word)
    print(r)