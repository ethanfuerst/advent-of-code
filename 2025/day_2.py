# https://adventofcode.com/2025/day/2

with open('2025/inputs/day_2.txt', 'r') as file:
    data = file.read()

data = data.split(',')
total = 0
for i in data:
    split_str = i.split('-')
    start = int(split_str[0])
    end = int(split_str[1])
    for j in range(start, end + 1):
        str_j = str(j)
        len_j = len(str_j)
        if len_j % 2 == 0:
            mid = int((len_j/2))
            s = str_j[0:mid]
            f = str_j[mid:]
            if s == f:
                total += j

print(total)

total = 0
for i in data:
    split_str = i.split('-')
    start = int(split_str[0])
    end = int(split_str[1])
    for j in range(start, end + 1):
        str_j = str(j)
        len_j = len(str_j)
        half_end = len_j // 2
        for k in range(half_end, 0, -1):
            sub = str_j[0: k]
            if len(str_j) % len(sub) == 0:
                num_reps = int(len(str_j) / len(sub))
                if str(int(sub)) == sub and str_j == sub * num_reps:
                    total += j
                    break

print(total)