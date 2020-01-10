class Solution:
    def simplifyPath(self, path: str) -> str:
        import re
        res = re.split('/+', path)
        stack = []
        for r in res:
            if r in ['', '.']:
                print('pass')
                pass
            elif r == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(r)
        return '/' + '/'.join(stack)

if __name__ == "__main__":
    path = "/../"
    r = Solution().simplifyPath(path)
    print(r)
