from aoc2023 import read_file_lines
import re
from itertools import product
import functools

testdata = read_file_lines("./input/day12-test-input.txt")

def test_parse():
    assert parse("???.### 1,1,3") ==  ("UUU.SSS", (1,1,3))
    assert parse(".??..??...?##. 1,1,3") == (".UU..UU...USS.", (1,1,3))
    assert parse("?#?#?#?#?#?#?#? 1,3,1,6") == ('USUSUSUSUSUSUSU', (1, 3, 1, 6))
    assert parse("????.#...#... 4,1,1") == ("UUUU.S...S...", (4, 1, 1))
    
    
def parse(line):
    """Parse a line of input into a list of strings and a list of tuples"""
    line = line.replace("?", "U")
    line = line.replace("#", "S")
    springs, checksums = line.split(' ')
    checksums = [int(i) for i in checksums.split(",")]
    return springs, tuple(checksums)

def test_parse_all():
    if testdata:
        assert parse_all(testdata) == [('UUU.SSS', (1, 1, 3)), 
                                       ('.UU..UU...USS.', (1, 1, 3)), 
                                       ('USUSUSUSUSUSUSU', (1, 3, 1, 6)), 
                                       ('UUUU.S...S...', (4, 1, 1)), 
                                       ('UUUU.SSSSSS..SSSSS.', (1, 6, 5)), 
                                       ('USSSUUUUUUUU', (3, 2, 1))]

def parse_all(data):
    parsed = []
    for line in data:
        parsed.append(parse(line))
    return parsed

def test_get_score():
    assert get_score('S.S.SSS') == (1,1,3)
    assert get_score('S.....SSS....SS.S') == (1,3,2,1)
    assert get_score('..S..S....SSS.') == (1,1,3)
    
def get_score(data):
    springs = re.split(r'\.+', data)
    springs = [s for s in springs if s]
    return tuple(len(s) for s in springs)
    
def test_get_combos():
    assert get_combos('UUU.SSS') == ['SSS.SSS','SS..SSS','S.S.SSS','S...SSS','.SS.SSS','.S..SSS','..S.SSS','....SSS']
    assert get_combos('UUUU.S...S...') == ['SSSS.S...S...', 'SSS..S...S...', 'SS.S.S...S...', 'SS...S...S...', 'S.SS.S...S...', 'S.S..S...S...', 'S..S.S...S...', 'S....S...S...', '.SSS.S...S...', '.SS..S...S...', '.S.S.S...S...', '.S...S...S...', '..SS.S...S...', '..S..S...S...', '...S.S...S...', '.....S...S...']

def get_combos(s):
        # Split the string into parts: 'U' parts and non-'U' parts
    parts = []
    temp = ""
    for char in s:
        if char == 'U':
            if temp:
                parts.append(temp)
                temp = ""
            parts.append('U')
        else:
            temp += char
    if temp:
        parts.append(temp)

    # Generate all combinations for the 'U' parts
    combinations = []
    for part in parts:
        if part == 'U':
            combinations.append(['S', '.'])
        else:
            combinations.append([part])

    # Use itertools.product to generate cartesian product of combinations
    all_combinations = list(product(*combinations))

    # Join the parts to form complete strings
    return [''.join(comb) for comb in all_combinations]


def test_score_combos():
    assert score_combos(get_combos('UUU.SSS'),(1,1,3)) == 1
    assert score_combos(get_combos('.UU..UU...USS.'), (1, 1, 3)) == 4
    
def score_combos(combos, checksums):
    score = 0
    for combo in combos:
        if get_score(combo) == checksums:
            score += 1
    return score

def test_score_all_combos():
    if testdata:
        assert score_all_combos(parse_all(testdata)) == 21
        

def score_all_combos(lines):
    total = 0
    for line in lines:
        total += score_combos(get_combos(line[0]), line[1])
    return total

# part2 credit goes to: 
# https://github.com/morgoth1145/advent-of-code/blob/54c79b33cd38f77240d7133bc4458755cefc2ce3/2023/12/solution.py

def count_matches2(pattern, splits):
    @functools.cache
    def gen(rem_pattern, rem_len, rem_splits):
        if len(rem_splits) == 0:
            if all(c in '.U' for c in rem_pattern):
                return 1
            return 0

        a = rem_splits[0]
        rest = rem_splits[1:]
        after = sum(rest) + len(rest)

        count = 0

        for before in range(rem_len-after-a+1):
            cand = '.' * before + 'S' * a + '.'
            if all(c0 == c1 or c0=='U'
                   for c0,c1 in zip(rem_pattern, cand)):
                rest_pattern = rem_pattern[len(cand):]
                count += gen(rest_pattern, rem_len-a-before-1, rest)

        return count

    return gen(pattern, len(pattern), tuple(splits))

def test_part2_data():
    assert part2_data('UUU.SSS',(1,1,3)) == ('UUU.SSSUUUU.SSSUUUU.SSSUUUU.SSSUUUU.SSS', (1,1,3,1,1,3,1,1,3,1,1,3,1,1,3))

def part2_data(a,b):
    return ('U'.join((a,a,a,a,a)), b*5)

def test_part2():
    if testdata:
        assert part2(parse_all(testdata)) == 525152

def part2(data):
    total = 0
    for a,b in data:
        aa,bb = part2_data(a,b)
        total += count_matches2(aa,bb)
    return total


input = read_file_lines("./input/day12-input.txt")
if input:
    print('part1', score_all_combos(parse_all(input)))
    print('part2', part2(parse_all(input)))
          