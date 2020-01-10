# comment 用str然后切片时间复杂度很高。用list然后pop比较好
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ''
        for c in S:
            stack += c
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack = stack[:-2]
        return stack

if __name__ == "__main__":
    S = 'abbaca'
    r = Solution().removeDuplicates(S)
    print(r)        