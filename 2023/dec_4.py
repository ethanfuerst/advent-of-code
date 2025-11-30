#%%
import re

# part 1
# get list of guesses and list of nums_to_check

with open("inputs/dec_4.txt", "r") as f:
    data = f.read().splitlines()

pattern = re.compile(r'(\d+(?:\s+\d+)*)\s*\|\s*(\d+(?:\s+\d+)*)')

total_score = 0

for i in data:
    match = pattern.search(i)

    guesses = match.group(1).split()
    nums_to_check = match.group(2).split()
    
    card_total = 0
    for check in nums_to_check:
        if check in guesses:
            card_total += 1
    if card_total > 0:
        card_total = 2 ** (card_total - 1)

    total_score += card_total
    
print(total_score)

# iterate through nums to check
# if num is in guesses, add to count
# if count = 1 then add 2

#%%
# part 2

# hashmap of scores

with open("inputs/dec_4.txt", "r") as f:
    data = f.read().strip().splitlines()

new_pattern = re.compile(r'Card\s+(\d+):\s*(\d+(?:\s+\d+)*)\s*\|\s*(\d+(?:\s+\d+)*)')

scoreboard = {i: 0 for i in range(1, len(data) + 1)}

def add_to_scoreboard(num):
    scoreboard[num] += 1
    
def get_score_of_card(guesses, nums_to_check):
    # could also use set intersection
    card_total = 0
    for check in nums_to_check:
        if check in guesses:
            card_total += 1
    return card_total

for i in data:
    match = new_pattern.search(i)

    game_num = int(match.group(1))
    guesses = match.group(2).split()
    nums_to_check = match.group(3).split()
    scoreboard[game_num] += 1

    card_total = get_score_of_card(guesses, nums_to_check)
    
    for k in range(card_total):
        # add the number of cards of the game_num to each of the next game_nums
        scoreboard[game_num + 1 + k] += scoreboard[game_num]
    print(scoreboard)
    
sum(scoreboard.values())



# %%
