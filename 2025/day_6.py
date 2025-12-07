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

nums = []
for i in data[:-1]:
    nums.append([k for k in i])

total = 0
ops_count = len(operations) - 1
str_list = []
for i in range(len(nums[0]) - 1, -2, -1):
    str_ = ''
    for k in range(len(nums)):
        str_ += nums[k][i]
    if str_ == ' ' * len(nums) or i == -1:
        if operations[ops_count] == '+':
            total += sum(str_list)
        else:
            mult = 1
            for j in str_list:
                mult *= j
            total += mult
        ops_count -= 1
        str_list = []
    else:
        str_list.append(int(str_))

print(total)
