class Solution:
    def convert(self, s: str, numRows: int) -> str:
        convert = ['' for _ in range(numRows)]
        for i, c in enumerate(s):
            block = i // (2*numRows - 2)
            num = i % (2*numRows - 2)
            print(block, num)
            if num < numRows:
                row = num
                convert[row] += c
                # column = block * (numRows - 1)
            else:
                row = 2*numRows - num - 2
                convert[row] += c
        print(convert)
        return ''.join(convert)


if __name__ == "__main__":
    s = '0123456789'
    s = 'LEETCODEISHIRING'
    numRows = 4
    r = Solution().convert(s, numRows)
    print(r)