import sys
import math
from collections import defaultdict


def process_line(line: str, num: int):
    global data
    global copies
    global answer
    answer += copies[num]
    _, tmp = line.split(":")
    win, you = tmp.split("|")
    win = set(win.split())
    you = set(you.split())
    inter = win & you
    if len(inter) > 0:
        amount = copies[num]
        for i in range(len(inter)):
            copies[num+i+1] += 1 * amount


answer = 0
lines = []
data = []
line_num = 0
copies = defaultdict(lambda: 1)
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    process_line(line, line_num)
    line_num += 1
    print(copies)


[print(line) for line in lines]
print("=" * 40)
print(answer)
