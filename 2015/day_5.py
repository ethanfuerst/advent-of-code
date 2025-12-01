# https://adventofcode.com/2015/day/5

with open('2015/inputs/day_5.txt', 'r') as file:
    data = file.read().splitlines()

def contains_vowels(str_, num_vowels):
    fin_word = ''
    for chr in str_:
        if chr in 'aeiou':
            fin_word += chr
    
    return len(fin_word) >= num_vowels

def has_a_double(str_):
    i, j = 0, 1

    while j < len(str_):
        if str_[i] == str_[j]:
            return True

        i += 1
        j += 1

    return False

def missing_certain_strings(str_):
    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for i in bad_strings:
        if i in str_:
            return False

    return True

nice_strings = []
for i in data:
    if contains_vowels(i, 3) and has_a_double(i) and missing_certain_strings(i):
        nice_strings.append(i)

print(f'Number of nice strings with first set of rules: {len(nice_strings)}')

def has_pairs(str_):
    i, j = 0, 2
    left_part = str_[i:j]
    
    # need to think about this
    return False

def has_sandwich(str_):
    i, j = 0, 2

    while j < len(str_):
        if str_[i] == str_[j]:
            return True

        i += 1
        j += 1

    return False

nice_strings = []
for i in data:
    if has_pairs(i) and has_sandwich(i):
        nice_strings.append(i)

print(f'Number of nice strings with second set of rules: {len(nice_strings)}')