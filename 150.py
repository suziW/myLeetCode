from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                stack.append(int(1/stack.pop() * stack.pop()))
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    r = Solution().evalRPN(tokens)
    print(r)