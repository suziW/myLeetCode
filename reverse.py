class Solution:

    def reverse(self, x: int) -> int:
        rl = []
        plus_minus = x >= 0
        x = abs(x)
        record = False
        for i in range(9, -1, -1):
            if x // 10**i != 0:
                record = True
            if record:
                rl.append(x // 10**i)
            x = x % 10**i
        print(rl)

        y = 0
        for i in range(len(rl)):
            y += rl[i] * 10**i

        if plus_minus == False:
            y = -y
        if y < -2**31 or y > 2**31 - 1:
            y = 0

        return y


if __name__ == "__main__":
    r = Solution().reverse(-2**21)
    print(-2**21)
    print(r)