# https://adventofcode.com/2025/day/6

with open('2025/inputs/day_6.txt', 'r') as file:
    data = file.read().splitlines()

nums = []
operations = []
for i in data[:-1]:
    nums.append([int(k) for k in i.split(' ') if k != ''])
operations = [k for k in data[-1].split(' ') if k != '']

total = 0
for num, op in enumerate(operations):
    sub_total = 0
    if op == '+':
        for line in nums:
            sub_total += line[num]
    else:
        mult = 1
        for line in nums:
            mult *= line[num]
        sub_total = mult
    total += sub_total
print(total)