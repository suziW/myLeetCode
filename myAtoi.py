import re


class Solution:

    def myAtoi(self, s: str) -> int:
        m = re.findall('[\+\-]?\d+', s.lstrip())
        print(m)
        return max(
            min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 1 << 31 - 1),
            -1 << 31)


if __name__ == "__main__":
    s = ' -1243, 13421'
    r = Solution().myAtoi(s)
    print('result is :', r)