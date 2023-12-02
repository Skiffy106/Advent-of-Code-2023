import sys

answer = 0
game_num = 1
for line in sys.stdin:
    line = line.strip()
    line = line.split(":")[1].strip()
    grabs = [x.strip() for x in line.split(";")]
    max_color = {"red": 0, "green": 0, "blue": 0}
    valid_line = True
    for grab in grabs:
        values = [x.strip() for x in grab.split(",")]
        for i in values:
            amount, color = i.split()
            max_color[color] = max(max_color[color], int(amount))
    answer += max_color["red"] * max_color["green"] * max_color["blue"]
    game_num += 1

print(answer)
