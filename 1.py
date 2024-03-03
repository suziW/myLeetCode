import sys

for line in sys.stdin:
    day = int(line[0])
    print(day)


def maxH(day):
    if day == 0:
        return 0
    h += maxH(day - 1)
