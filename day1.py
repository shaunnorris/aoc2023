import pytest
from aoc2023 import read_file_lines

def test_extract_digits():
    assert extract_digits("1abc2") == (12)
    assert extract_digits("pqr3stu8vwx") == (38)
    assert extract_digits("a1b2c3d4e5f") == (15)
    assert extract_digits("treb7uchet") == (77)
    assert extract_digits("abc123xyz") == (13)  # Including previous tests for thoroughness
    assert extract_digits("1234") == (14)
    assert extract_digits("a1b2c3") == (13)
    assert extract_digits("7abc") == (77)

def extract_digits_old(input_string):
    """Extract the first and last digits from a string"""
    digits = [char for char in input_string if char.isdigit()]
    if len(digits) == 0:
        return None
    else:
        return (int(digits[0]) * 10) + int(digits[-1])

def extract_digits(s):
    def find_first_digit(ss):
        for char in ss:
            if char.isdigit():
                return int(char)
    
    first_digit = find_first_digit(s)
    last_digit = find_first_digit(reversed(s))

    
    return first_digit*10 + last_digit


def solve_part1(input):
    puzzle_sum = 0
    for line in input:
        puzzle_sum += extract_digits(line)
    return puzzle_sum

def test_solve_part1():
    assert solve_part1(["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]) == 142



def replace_text_old(s):
    number_map = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    result = list(s)
    i = 0
    while i < len(result):
        replaced = False
        # Check for each spelled number in order of length
        for length in range(5, 2, -1):  # Check 5, 4, 3 characters length
            if i + length <= len(result):
                substring = ''.join(result[i:i+length])
                if substring in number_map:
                    # Replace the first character of the found spelled word with the digit
                    result[i] = number_map[substring]
                    replaced = True
                    break
        i += 1  # Move forward by one position regardless of whether a replacement was made or not

    return ''.join(result)

        
def test_parse_part2():
    assert extract_digits_part2("abcone2threexyz") == (13)
    assert extract_digits_part2("two1nine") == (29)
    assert extract_digits_part2("sevenine") == (79)
    assert extract_digits_part2("eighthree") == (83)
    assert extract_digits_part2("eightwothree") == (83)
    assert extract_digits_part2("xtwone3four") == (24)
    assert extract_digits_part2("4nineeightseven2") == (42)
    assert extract_digits_part2("zoneight234") == (14)
    assert extract_digits_part2("7pqrstsixteen") == (76)
    assert extract_digits_part2("gndxnlmnrmnk29qkfxfoursnnbvjtq") == (24)


def extract_digits_part2(s):
    def find_first_digit_part2(s,direction):

        stack = []
        if direction == "forward":
            number_map = {
                "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9"
            }
        elif direction == "backward":
            number_map = {
                "eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5",
                "xis": "6", "neves": "7", "thgie": "8", "enin": "9"
            }
        for char in s:
            stack.append(char)
            if len(stack)  >=3:
                for start in range(len(stack)-2):
                    word = ''.join(stack[start:])
                    if word in number_map:
                        return int(number_map[word])
            if len(stack) > 5:
                stack.pop(0)    
            if char.isdigit():
                return int(char)
        return None
    
    first_digit = find_first_digit_part2(s,'forward')
    last_digit = find_first_digit_part2(reversed(s),'backward')
    return first_digit*10 + last_digit

def solve_part2(input):
    puzzle_sum = 0
    for line in input:
        puzzle_sum += extract_digits_part2(line)
    return puzzle_sum

def test_solve_part2():
    assert solve_part2(["two1nine",
                        "eightwothree",
                        "abcone2threexyz",
                        "xtwone3four",
                        "4nineeightseven2",
                        "zoneight234",     
                        "7pqrstsixteen"
                        ]) == 281


input_file = './input/day1-input.txt'
input = read_file_lines(input_file)
if input:
    print("Part 1:", solve_part1(input))
    print("Part 2:", solve_part2(input))