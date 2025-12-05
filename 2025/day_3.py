# https://adventofcode.com/2025/day/3
from itertools import combinations
import time

with open('2025/inputs/day_3.txt', 'r') as file:
    data = file.read().splitlines()

total = 0
for line in data:
    lag, lead = 0, 1
    len_ = len(line)
    line_max = 0
    while lag < len_ - 1:
        lead = lag + 1
        for i in range(lead, len_):
            to_check = int(line[lag] + line[i])
            if line_max == 0 or line_max < to_check:
                line_max = to_check
        lag += 1
    total += line_max

print(total)

# works in test case but too expensive to get correct answer with all data
s = int(time.time())
total = 0
count = 0
for line in data:
    max = 0
    for i in combinations(line, 12):
        m = int(''.join(i))
        if m > max:
            max = m
    total += max
    count += 1
    nt = int(time.time())
    print(nt - s, count, max)

print(total)
