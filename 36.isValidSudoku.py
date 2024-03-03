from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = [[], [], [], [], [], [], [], [], []]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    k = i // 3 * 3 + j // 3
                    memo[int(board[i][j]) - 1].append((i, j, k))
        print(memo)
        valid = True
        for coords in memo:
            print('------------------------------------------------')
            print(coords)
            if not self.isValidCoords(coords):
                valid = False
                break
        return valid

    def isValidCoords(self, coords):
        if coords == []:
            return True

        ilist, jlist, klist = [], [], []
        for c in coords:
            ilist.append(c[0])
            jlist.append(c[1])
            klist.append(c[2])
        print(ilist, jlist, klist)
        return len(ilist) == len(set(ilist)) and len(jlist) == len(
            set(jlist)) and len(klist) == len(set(klist))


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # a = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #      [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #      [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    r = Solution().isValidSudoku(board)
    print(r)
|3|4|5|6|7|8|9|
|.|.|.|.|.|5|.|
