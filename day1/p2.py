import sys

answer = 0
words = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def parse_line(line: str) -> None:
    # sliding window solution
    global answer
    line_len = len(line)
    digits = []
    left = 0
    right = 0
    while right < line_len:
        char = line[right]
        if char.isdigit():
            digits.append((right, char))
            left = right + 1
        else:
            # march left pointer towards right
            start = left
            reset = True
            while left < right:
                word = line[left:right+1]
                if word in words:
                    digits.append((left, words[word]))
                    left = right
                    reset = False
                else:
                    left += 1
            # if no word found reset left
            if reset:
                left = start
        right += 1
    start = digits[0]
    end = digits.pop()
    answer += int(start[1] + end[1])


for line in sys.stdin:
    line = line.strip()
    # print(line)
    parse_line(line)


print(answer)
