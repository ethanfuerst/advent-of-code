# https://adventofcode.com/2023/day/2

with open("inputs/dec_2.txt", "r") as f:
    data = f.read().splitlines()

r_total = 12
g_total = 13
b_total = 14

total = 0
for game in data:
    # print(game)
    game = game.replace(':', ',').replace(';', ',').split(',')
    game_num = int(game[0].split(' ')[-1])
    game = game[1:]
    
    for grab in game:
        # print(grab)
        grab = grab.strip(' ').split(' ')
        num_boxes = int(grab[0])
        color = grab[1]
        if (color == 'red' and num_boxes > r_total) or (color == 'green' and num_boxes > g_total) or (color == 'blue' and num_boxes > b_total):
            # if not possible, break
            # print('not possible')
            break
    else:
        # print('possible')
        total += game_num
        pass

# 2776
print('part 1 total is', total)

#%%
# In each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

with open("inputs/dec_2.txt", "r") as f:
    data = f.read().splitlines()

total = 0
for game in data:
    print(game)
    game = game.replace(':', ',').replace(';', ',').split(',')
    game_num = int(game[0].split(' ')[-1])
    game = game[1:]
    
    # set mins for each color
    r_min = 0
    b_min = 0
    g_min = 0
    
    for grab in game:
        grab = grab.strip(' ').split(' ')
        num_boxes = int(grab[0])
        color = grab[1]
        
        # check num_boxes against each min
        if color == 'red' and num_boxes > r_min:
            r_min = num_boxes
        elif color == 'green' and num_boxes > g_min:
            g_min = num_boxes
        elif color == 'blue' and num_boxes > b_min:
            b_min = num_boxes
        else:
            # just felt weird not adding an else clause
            pass
    print(game, r_min, b_min, g_min)
    
    total += (r_min * b_min * g_min)

# 68638
print('part 2 total is', total)
