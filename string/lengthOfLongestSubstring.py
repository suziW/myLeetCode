class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        char_dict = {}

        for i, c in enumerate(s):
            if c in char_dict:
                l = max(l, char_dict[c] + 1)
            longest = max(longest, i - l + 1)
            char_dict[c] = i
        
        return longest


if __name__ == "__main__":
    s = 'abba'
    r = Solution().lengthOfLongestSubstring(s)
    print(r)