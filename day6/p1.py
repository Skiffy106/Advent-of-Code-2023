# import sys
# import math


line1 = input()
line2 = input()
tmp1 = line1.split(":")[1]
tmp2 = line2.split(":")[1]
max_times = [int(x) for x in tmp1.split()]
best_dists = [int(x) for x in tmp2.split()]
print(max_times)
print(best_dists)

# f(x) = x(max_time - x)
# for each integer value x
# find num occurrences where f(x) > best_dist

answers = []
for idx in range(len(max_times)):
    max_time = max_times[idx]
    best_dist = best_dists[idx]
    # print(max_time, best_dist)
    tally = 0
    for hold_time in range(1, max_time):
        dist = hold_time * (max_time - hold_time)
        if dist > best_dist:
            # print(max_time, hold_time, dist)
            tally += 1
    answers.append(tally)

print(answers)
product = 1
for val in answers:
    if val > 0:
        product *= val
print(product)
