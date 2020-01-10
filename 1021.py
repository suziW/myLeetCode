class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        count = 0
        start = -1
        for i, th in enumerate(S):
            if th == '(':
                count += 1
            else:
                count -= 1
            print(count, th, start, i)
            if count == 0:
                res += S[start+2:i]
                start = i
        return res

if __name__ == "__main__":
    S = "(()())(())(()(()))"
    r = Solution().removeOuterParentheses(S)
    print(r)