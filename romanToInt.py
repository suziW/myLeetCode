import re


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        spacial = [d[c] for c in re.findall('IV|IX|XL|XC|CD|CM', s)]
        rest = [d[c] for c in re.sub('IV|IX|XL|XC|CD|CM', '', s)]
        return sum(spacial) + sum(rest)


if __name__ == '__main__':
    s = 'MCMXCIV'
    r = Solution().romanToInt(s)
    print(r)
