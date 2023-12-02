import sys

answer = 0
for line in sys.stdin:
    line = line.strip()
    first = ""
    last = ""
    for char in line:
        if char.isdigit():
            if not first:
                first = char
            last = char
    answer += int(first + last)

print(answer)
