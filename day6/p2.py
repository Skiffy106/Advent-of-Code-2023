# import sys
# import math


line1 = input()
line2 = input()
tmp1 = line1.split(":")[1]
tmp2 = line2.split(":")[1]
max_time = int("".join(tmp1.split()))
best_dist = int("".join(tmp2.split()))
print(max_time)
print(best_dist)

# f(x) = x(max_time - x)
# for each integer value x
# find num occurrences where f(x) > best_dist

answers = []
# max_time = max_times[idx]
# best_dist = best_dists[idx]
answer = 0
for hold_time in range(1, max_time):
    dist = hold_time * (max_time - hold_time)
    if dist > best_dist:
        # print(max_time, hold_time, dist)
        answer += 1

print(answer)
