import sys

answer = 0
game_num = 1
max_color = {"red": 12, "green": 13, "blue": 14}
for line in sys.stdin:
    line = line.strip()
    line = line.split(":")[1].strip()
    grabs = [x.strip() for x in line.split(";")]
    valid_line = True
    for grab in grabs:
        values = [x.strip() for x in grab.split(",")]
        for i in values:
            amount, color = i.split()
            if int(amount) > max_color[color]:
                valid_line = False
                break
    if valid_line:
        answer += game_num
    game_num += 1

print(answer)
