# https://adventofcode.com/2015/day/3

with open('2015/inputs/day_3.txt', 'r') as file:
    data = file.read()

def get_new_coords(char, coords):
    if char == '>':
        return (coords[0] + 1, coords[1])
    elif char == '<':
        return (coords[0] -1, coords[1])
    elif char == '^':
        return (coords[0], coords[1] + 1)
    elif char == 'v':
        return (coords[0], coords[1] - 1)
    
coords = [(0, 0)]
for i in data:
    prev_coords = coords[-1]

    new_coords = get_new_coords(i, prev_coords)
    
    coords.append(new_coords)

print(f'Unique houses delivered to: {len(set(coords))}')
    
coords = [(0, 0)]
prev_santa_coords = (0, 0)
prev_robo_santa_coords = (0, 0)

for i, j in enumerate(data):
    if i % 2 == 0:
        new_coords = get_new_coords(j, prev_santa_coords)
        
        prev_santa_coords = new_coords
    else:
        new_coords = get_new_coords(j, prev_robo_santa_coords)
        
        prev_robo_santa_coords = new_coords

    coords.append(new_coords)

print(f'Unique houses delivered to with robo-santa: {len(set(coords))}')
