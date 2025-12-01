# https://adventofcode.com/2015/day/4

import hashlib

i = 'yzbqklnj'

def check_starts_with_zeros(num_zeros):
    starts_with_zeros = False
    start_number = 1

    while not starts_with_zeros:
        new_str = f'{i}{start_number}'
        res = hashlib.md5(new_str.encode()).hexdigest()

        str_match = '0' * num_zeros
        if res[:num_zeros] == str_match:
            starts_with_zeros = True

        start_number += 1

    return start_number

print(f'Lowest number that hash starts with 5 zeros: {check_starts_with_zeros(5)}')
print(f'Lowest number that hash starts with 6 zeros: {check_starts_with_zeros(6)}')
