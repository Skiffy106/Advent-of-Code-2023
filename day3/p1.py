import sys


def process_line(line: str, row: int) -> list:
    data_line = []
    digit = False
    for idx, char in enumerate(line):
        if char.isdigit():
            if digit:
                data_line[-1][0] += char
            else:
                data_line.append([char, (row, idx)])
            digit = True
        else:
            digit = False
            # if not char.isalnum() and char != ".":
            #     data_line.append([char, (row, idx)])
    return data_line


def isValid(number: str, start_row: int, start_col: int, max_rows: int, max_cols: int) -> bool:
    global lines
    length = len(number)
    row = start_row - 1
    if row >= 0:
        for col in range(start_col-1, start_col + length + 1):
            print(lines[row-1][col])
            if col >= 0 and not lines[row-1][col].isalnum() and lines[row-1][col] != ".":
                return True
    print(lines[start_row][start_col-1])
    if start_col - 1 >= 0 and not lines[start_row][start_col-1].isalnum() and lines[start_row][start_col-1] != ".":
        return True
    print(lines[start_row][start_col+length])
    if start_col+length < max_cols and not lines[start_row][start_col+length].isalnum() and lines[start_row][start_col+length] != ".":
        return True
    row = row = start_row + 1
    if row < max_rows:
        for col in range(start_col-1, start_col + length + 1):
            print(lines[start_row][start_col+length])
            if row + 1 < max_rows and not lines[row+1][col].isalnum() and lines[row+1][col] != ".":
                return True
    return False


answer = 0
lines = []
data = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    row = len(lines) - 1
    data.append(process_line(line, row))

max_rows = len(lines)
max_cols = len(lines[0])
for row, data_line in enumerate(data):
    for poi in data_line:
        number = poi[0]
        assert (row == poi[1][0])
        row, col = poi[1]

        if isValid(number, row, col, max_rows, max_cols):
            answer += int(number)

# row, col = symbols.pop()
# if row - 1 >= 0 and lines[]

# print(lines)
# print("="*20)
# print(data)
# print("="*20)
# print(answer)
