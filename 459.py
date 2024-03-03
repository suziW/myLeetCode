class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def rightSheft(s):
            return s[-1] + s[:-1]
        s_shift = s
        for _ in range(len(s)>>1):
            s_shift = rightSheft(s_shift)
            print(s_shift, s)
            if s_shift == s:
                return True
        return False

if __name__ == "__main__":
    s = "abab"
    r = Solution().repeatedSubstringPattern(s)
    print(r)