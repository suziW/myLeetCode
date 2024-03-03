from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

if __name__ == "__main__":
    ops = ["5","-2","4","C","D","9","+","+"]
    r = Solution().calPoints(ops)
    print(r)