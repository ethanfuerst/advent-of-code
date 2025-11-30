with open('2015/inputs/day_1.txt', 'r') as file:
    data = file.read()

floor = 0
message_printed = False
for i, char in enumerate(data):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1 and not message_printed:
        print(f'First entering basement at position: {i + 1}')
        message_printed = True
        
print(f'Final floor: {floor}')
