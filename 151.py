import re
class Solution:
    def reverseWords(self, s: str) -> str:
        l = re.findall('[^ ]+', s)
        return ' '.join(l[::-1])

if __name__ == "__main__":
    s = 'hello  the fucking world! '
    r = Solution().reverseWords(s)
    print(r)