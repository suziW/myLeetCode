from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                r.append(s)
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        backtrack()
        return r

if __name__ == "__main__":
    n = 3
    r = Solution().generateParenthesis(n)
    print(r)