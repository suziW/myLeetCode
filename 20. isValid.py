class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stack = []
        smap = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            print('===in', stack)
            if c in smap.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and smap[stack[-1]] == c:
                    stack.pop(-1)
                else:
                    valid = False
                    break
            print('===out', stack)
        if len(stack) != 0:
            valid = False
        return valid


if __name__ == "__main__":
    s = "]"
    r = Solution().isValid(s)
    print(r)