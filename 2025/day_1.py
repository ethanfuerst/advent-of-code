# https://adventofcode.com/2025/day/1

with open('2025/inputs/day_1.txt', 'r') as file:
    data = file.read().splitlines()

dial_point = 50
final_count = 0
for i in data:
    direction = i[0]
    direction_count = int(i[1:])

    if direction == 'R':
        dial_point += direction_count
    else:
        dial_point -= direction_count

    if dial_point < 0:
        dial_point = (dial_point + 100 * ((dial_point // 100) + 1)) % 100
    if dial_point > 99:
        dial_point = dial_point % 100
        
    if dial_point % 100 == 0:
        final_count += 1

print(f'first answer is: {final_count}')

dial_point = 50
final_count = 0
for i in data:
    direction = i[0]
    direction_count = int(i[1:])

    # increment dial_count and direction count
    # subtract one from direction count
    # mod 100, if it hits 0 then record it
    if direction == 'R':
        while direction_count > 0:
            dial_point += 1
            dial_point = dial_point % 100
            direction_count -= 1
            if dial_point == 0:
                final_count += 1
    else:
        while direction_count > 0:
            dial_point -= 1
            dial_point = dial_point % 100
            direction_count -= 1
            if dial_point == 0:
                final_count += 1


print(f'second answer is: {final_count}')
