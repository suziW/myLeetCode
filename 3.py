class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        chars = {}
        for i, c in enumerate(s):
            if c in chars:
                left = max(left, chars[c] + 1)
            chars[c] = i
            longest = max(longest, i - left + 1)
        return longest

if __name__=='__main__':
    s = 'abba'
    r = Solution().lengthOfLongestSubstring(s)
    print(r)