import re
class Solution:
    def countSegments(self, s: str) -> int:
        s = re.findall('[^ ]+', s)
        print(s)

if __name__ == "__main__":
    s = 'qqqq'
    r = Solution().countSegments(s)
    print(r)