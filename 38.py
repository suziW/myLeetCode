class Solution:
    def countAndSay(self, n: int) -> str:
        def calNext(s):
            r = ''
            temp = s[0]
            count = 0
            for c in s:
                if c == temp:
                    count += 1
                else:
                    r += str(count) + temp
                    temp = c
                    count = 1
            r += str(count) + temp
            return r
        s = '1'
        for i in range(n-1):
            print(s)
            s = calNext(s)
        return s
        
if __name__ == "__main__":
    n = 30
    r = Solution().countAndSay(n)
    print(r)