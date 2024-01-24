import sys
import math

answer = 0
lines = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    _, data = line.split(":")
    win, you = data.split("|")
    win = set(win.split())
    you = set(you.split())
    inter = win & you
    # print(inter)
    if len(inter) >= 1:
        answer += math.pow(2, len(inter) - 1)
    # print(math.pow(2, len(win & you) - 1))


[print(line) for line in lines]
print("=" * 40)
print(answer)
