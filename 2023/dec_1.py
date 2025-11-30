# https://adventofcode.com/2023/day/1

with open("inputs/dec_1.txt", "r") as f:
    data = f.read().splitlines()

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}


def solution_1(data):
    total = 0

    for i in list(data):
        first_val = 0
        last_val = 0
        for val in range(len(i)):
            if str(i[val]) in digits.keys():
                first_val = i[val]
                break
        for val in range(len(i) - 1, -1, -1):
            if str(i[val]) in digits.keys():
                last_val = i[val]
                break
        print(int(str(first_val) + str(last_val)))
        total += int(str(first_val) + str(last_val))

    return total

# 54239
print("Part 1 solution:", solution_1(data))

# Your calculation isn't quite right.
# It looks like some of the digits are actually spelled out with letters.
# What is the sum of all of the calibration values?

def replacer(code):
    # use hash map to get where first value of all strings are
    # then replace the number with the lowest first value
    # repeat until all first values are -1 so all numbers are replaced
    # think this will work but not sure about how this works with overlap backwards

    ref_list = []
    max_num = 0
    while max_num > -1:
        for num in digits.values():
            number_loc = code.find(num)
            ref_list.append(number_loc)
            max_num = ref_list.max()

        # find all number locations and put them in a list
        ref_list.clear()

    return


# recursive function
# find all numbers locations
# replace lowest one
# repeat
# if lowest is -1 then break


def solution_2(data):
    cleaned_data = []

    return solution_1(cleaned_data)


print("Part 2 solution:", solution_2(data))
