class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0: stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


if __name__ == "__main__":
    num = "1432219"
    k = 3
    r = Solution().removeKdigits(num, k)
    print(r)