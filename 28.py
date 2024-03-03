class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='': return 0
        if len(needle) > len(haystack): return -1
        def calShitfDict(pattern):
            dic = {}
            for i in range(len(pattern)-1, -1, -1):
                if not dic.get(pattern[i]):
                    dic[pattern[i]] = len(pattern) - i
                dic['ot'] = len(pattern) + 1
            return dic
        dic = calShitfDict(needle)
        idx = 0
        while idx + len(needle) <= len(haystack):
            str_cut = haystack[idx:idx + len(needle)]
            if str_cut == needle: return idx
            else:
                if idx + len(needle) >= len(haystack): return -1
                if dic.get(haystack[idx + len(needle)]):
                    idx += dic[haystack[idx + len(needle)]]
                else:
                    idx += dic['ot']
        return -1

if __name__ == "__main__":
    haystack = 'hello'
    needle = 'llo'
    r = Solution().strStr(haystack, needle)
    print(r)