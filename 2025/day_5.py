# https://adventofcode.com/2025/day/5

with open('2025/inputs/day_5.txt', 'r') as file:
    data = file.read().splitlines()

ranges = []
nums = []
for i in data:
    if i == '':
        pass
    elif '-' in i:
        i = i.split('-')
        ranges.append((int(i[0]), int(i[1])))
    else:
        nums.append(int(i))

fresh = []
for i in nums:
    for j in ranges:
        if j[0] <= i and i <= j[1]:
            fresh.append(i)
            break

print(len(fresh))

ranges = sorted(ranges)
merged = []
for j in ranges:
    start = j[0]
    end = j[1]
    if not merged:
        merged.append([start, end])
    end_of_last_merged = merged[-1][-1]
    if start > merged[-1][-1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

total = 0
for m in merged:
    total += m[1] - m[0] + 1

print(total)
