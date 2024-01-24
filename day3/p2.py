import sys


def isSpecial(char) -> bool:
    if not char.isalnum() and char != ".":
        return True
    return False


def process_line(data: list, special: list, line: str, row: int):
    data_line = []
    special_line = []
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
            if isSpecial(char):
                special_line.append([char, (row, idx)])
            # if not char.isalnum() and char != ".":
            #     data_line.append([char, (row, idx)])
    data.append(data_line)
    special.append(special_line)


# def isValid(number: str, start_row: int, start_col: int, max_rows: int, max_cols: int) -> bool:
#     global lines
#     length = len(number)
#     # print("above")
#     # above number
#     if start_row - 1 >= 0:
#         for col in range(start_col-1, start_col + length + 1):
#             if col > max_cols:
#                 break
#             # print(lines[start_row - 1][col])
#             if start_row - 1 >= 0 and not lines[start_row - 1][col].isalnum() and lines[start_row - 1][col] != ".":
#                 return True
#     # print("left")
#     # print(lines[start_row][start_col-1])
#     # print((start_row, start_col-1))
#     # left of number
#     if start_col - 1 >= 0 and not lines[start_row][start_col-1].isalnum() and lines[start_row][start_col-1] != ".":
#         return True
#     # print("right")
#     # print(lines[start_row][start_col+length])
#     # print((start_row, start_col+length))
#     # right of number
#     if start_col + length < max_cols and not lines[start_row][start_col+length].isalnum() and lines[start_row][start_col+length] != ".":
#         return True
#     # below number
#     # print("below")
#     if start_row + 1 < max_rows:
#         for col in range(start_col-1, start_col + length + 1):
#             # print((start_row + 1, col))
#             # print(lines[start_row + 1][col])
#             if col > max_cols:
#                 break
#             if start_row + 1 < max_rows and not lines[start_row + 1][col].isalnum() and lines[start_row + 1][col] != ".":
#                 return True
#     return False

def crawl_neighbors(char, row, col, max_rows, max_cols):
    global lines
    global data
    global answer
    # top row
    # print(row, col)
    found = []
    if row - 1 >= 0:
        for poi in data[row-1]:
            num = poi[0]
            left = poi[1][1]
            right = left + len(num) - 1
            # 123
            # ..*
            # l.r
            if left <= col + 1:
                if right >= col - 1:
                    found.append(poi)
    for poi in data[row]:
        num = poi[0]
        left = poi[1][1]
        right = left + len(num) - 1
        # 123*...
        # or
        # ...*123
        if right == col - 1 or left == col + 1:
            found.append(poi)
    if row + 1 <= len(data):
        for poi in data[row+1]:
            num = poi[0]
            left = poi[1][1]
            right = left + len(num) - 1
            # ...*
            # 123.
            # l.r
            if left <= col + 1:
                if right >= col - 1:
                    found.append(poi)

    # print("neighbors:", found)

    if len(found) == 2:
        # print("found:", found[0][0], found[1][0])
        answer += int(found[0][0]) * int(found[1][0])
        # for col in range(row-1, col + length + 1):
        #     if col > max_cols:
        #         break
        #     # print(lines[start_row - 1][col])
        #     if start_row - 1 >= 0 and not lines[start_row - 1][col].isalnum() and lines[start_row - 1][col] != ".":
        #         return True


answer = 0
lines = []
data = []
special = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    row = len(lines) - 1
    process_line(data, special, line, row)

# print(data)
max_rows = len(lines)-1
max_cols = len(lines[0])-1
for row, special_line in enumerate(special):
    for poi in special_line:
        print("poi:", poi)
        char = poi[0]
        assert (row == poi[1][0])
        row, col = poi[1]

        if isSpecial(char):
            crawl_neighbors(char, row, col, max_rows, max_cols)
#         if isValid(number, row, col, max_rows, max_cols):
#             print(number, "Valid")
#             answer += int(number)
#         else:
#             print(number, "Not Valid")

# row, col = symbols.pop()
# if row - 1 >= 0 and lines[]

# print("="*20)
# [print(line) for line in lines]
# print("="*20)
# print(data)
# print("="*20)
# print(special)
# print("="*20)
print(answer)
