class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def go_stack(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack != []:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        stacks = go_stack(S)
        stackt = go_stack(T)
        print(stacks)
        print(stackt)
        return stackt == stacks

if __name__ == "__main__":
    S = "a##c"
    T = "#a#c"
    r = Solution().backspaceCompare(S, T)
    print(r)