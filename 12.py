class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        s = ''
        while i < len(l):
            if num >= l[i]:
                s += dic[l[i]]
                num -= l[i]
            else:
                i += 1
        return s

if __name__ == "__main__":
    num = 1996
    r = Solution().intToRoman(num)
    print(r)