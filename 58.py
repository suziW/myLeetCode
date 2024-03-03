import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = re.split(' ', s.rstrip())
        print(w)
        return len(w[-1])

if __name__ == "__main__":
    s = 'a  '
    r = Solution().lengthOfLastWord(s)
    print(r)