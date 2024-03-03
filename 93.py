from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def restore(r=[], count=0, ins='', s=''):
            if count > 4:
                return
            if count == 4 and s == '':
                r.append(ins[:-1])
                return
            if len(s) > 0:
                restore(r, count+1, ins+s[0]+'.', s[1:])
            if len(s) > 1 and s[0] != '0':
                restore(r, count+1, ins+s[:2]+'.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                restore(r, count+1, ins+s[:3]+'.', s[3:])
        r = []
        restore(r, 0, '', s)
        return r
            

if __name__ == "__main__":
    s = "25525511135"
    r = Solution().restoreIpAddresses(s)
    print(r)