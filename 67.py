class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = ''
        if len(a) < len(b):
            a, b = b, a
        adds = len(a)
        carry = 0
        for add in range(1, adds+1):
            b_ = 0
            if add <= len(b):
                b_ = int(b[-add])
            s = int(a[-add]) + b_ + carry
            print(s)
            s, carry = s % 2, s//2
            r = str(s) + r
            print(r, s ,carry)
        if carry:
            r = str(carry) + r
        return r

if __name__ == "__main__":
    a = '1010'
    b = '1011'
    r = Solution().addBinary(a, b)
    print(r)