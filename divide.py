class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        #把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                # print(result, count, 1 << count)
                result += 1 << count  #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result

        return max(min(result, (1 << 31) - 1), -1 << 31)


if __name__ == "__main__":
    dividend = -214748368
    divisor = -1
    r = Solution().divide(dividend, divisor)
    print(r)