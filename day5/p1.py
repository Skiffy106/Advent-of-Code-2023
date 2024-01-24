import sys
import math


def evaluate(conv_map, num):
    for dst_start, src_start, length in conv_map:
        dst_end = dst_start + length - 1
        src_end = src_start + length - 1
        # print(src_start, src_end, dst_start, dst_end)
        if num >= src_start and num <= src_end:
            # print(src_start, src_end, dst_start, dst_end)
            # print(dst_start, num, "-", src_start)
            return dst_start + (num - src_start)
    return num


lines = []
mode = "seeds"
seeds = []
soil_map = []
fert_map = []
water_map = []
light_map = []
temp_map = []
hum_map = []
loc_map = []
for line in sys.stdin:
    line = line.strip()
    # print(line, "|", mode)
    lines.append(line)
    if mode == "seeds":
        if len(line) == 0:
            mode = "soil"
            continue
        _, tmp = line.split(":")
        for i in tmp.split():
            seeds.append(int(i))
    elif mode == "soil":
        if len(line) == 0:
            mode = "fertilizer"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        soil_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "fertilizer":
        if len(line) == 0:
            mode = "water"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        fert_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "water":
        if len(line) == 0:
            mode = "light"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        water_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "light":
        if len(line) == 0:
            mode = "temp"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        light_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "temp":
        if len(line) == 0:
            mode = "hum"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        temp_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "hum":
        if len(line) == 0:
            mode = "loc"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        hum_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    elif mode == "loc":
        if len(line) == 0:
            mode = "final"
            continue
        if ":" in line:
            continue
        dst_start, src_start, range_len = [int(i) for i in line.split()]
        loc_map.append((dst_start, src_start, range_len))
        # print(dst_start, src_start, range_len)
    else:
        pass
        # print("Error")


# [print(line) for line in lines]
answers = []
print("=" * 20)
print(seeds)
print("=" * 20)
for seed in seeds:
    # print(seed)
    seed = evaluate(soil_map, seed)
    # print(seed)
    seed = evaluate(fert_map, seed)
    # print(seed)
    seed = evaluate(water_map, seed)
    # print(seed)
    seed = evaluate(light_map, seed)
    # print(seed)
    seed = evaluate(temp_map, seed)
    # print(seed)
    seed = evaluate(hum_map, seed)
    # print(seed)
    seed = evaluate(loc_map, seed)
    # print(seed)
    answers.append(seed)
    # print("=" * 20)

print(min(answers))

# [print(evaluate(soil_map, seed)) for seed in seeds]
# print(soil_map)
# print("=" * 20)
# print(fert_map)
