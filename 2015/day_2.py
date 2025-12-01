# https://adventofcode.com/2015/day/2

with open('2015/inputs/day_2.txt', 'r') as file:
    data = file.read().splitlines()

total_area = 0
total_ribbon = 0
for i in data:
    lwh_sorted = sorted([int(j) for j in i.split('x')])

    box_area = 2 * ((lwh_sorted[0] * lwh_sorted[1]) + (lwh_sorted[1] * lwh_sorted[2]) + (lwh_sorted[0] * lwh_sorted[2]))
    extra_area = lwh_sorted[0] * lwh_sorted[1]
    
    needed_area = box_area + extra_area
    total_area += needed_area
    
    ribbon_needed = (lwh_sorted[0] + lwh_sorted[1]) * 2
    ribbon_bow = (lwh_sorted[0] * lwh_sorted[1] * lwh_sorted[2])
    total_ribbon += ribbon_needed
    total_ribbon += ribbon_bow
    
print(f'Total area of wrapping paper needed: {total_area}')
print(f'Total length of ribbon needed: {total_ribbon}')
