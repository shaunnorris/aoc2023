from aoc2023 import read_file_lines
from itertools import combinations



def test_add_empty_rows():
    small_test_data = ["#...", "....", "..#.","...#"]
    assert add_empty_rows(small_test_data) == ["#...", "....", "....","..#.","...#"]
    
def add_empty_rows(data):
    """Add empty rows to the top and bottom of the data"""
    new_rows = []
    for row in data:
        if "#" in row:
            new_rows.append(row)
        else:
            new_rows.append(row)
            new_rows.append(row)
    return new_rows



test_data = read_file_lines("day11-test-input.txt")
test_data_expanded = read_file_lines("day11-test-expand.txt")


def test_expand():
    small_test_data = ["#...", "....", "..#.","...#"]
    assert expand(small_test_data) == ['#....', '.....', '.....', '...#.', '....#']
    assert expand(test_data) == test_data_expanded
    
def expand(data):
    expanded_rows = add_empty_rows(data)
    columns = transpose(expanded_rows)
    expanded_columns = add_empty_rows(columns)
    new_rows = transpose(expanded_columns)
    return new_rows

def transpose(strings):
    zipped = zip(*strings)
    transposed = [''.join(group) for group in zipped]
    return transposed

def test_find_galaxies():
    small_test_data = ["#...", "....", "..#.","...#"]
    assert find_galaxies(expand(small_test_data)) == [(0,0), (3,3), (4,4)]  
    assert find_galaxies(expand(test_data)) == [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]  
  
def find_galaxies(data):
    galaxies = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "#":
                galaxies.append((row, col))
    return galaxies

def test_get_combinations():
    small_test_data = ["#...", "....", "..#.","...#"]
    small_test_galaxies = find_galaxies(expand(small_test_data))
    assert get_combinations(small_test_galaxies) == [((0, 0), (3, 3)), ((0, 0), (4, 4)), ((3, 3), (4, 4))]
    test_galaxies = find_galaxies(expand(test_data))
    assert len(get_combinations(test_galaxies)) == 36
    
def get_combinations(galaxies):
    unique_combos = list(combinations(galaxies, 2))
    return unique_combos

def test_get_distance():
    assert get_distance((2,0), (7,12)) == 17
    
def get_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]) 

def test_get_all_distances():
    test_galaxy_pairs = get_combinations(find_galaxies(expand(test_data)))
    assert get_all_distances(test_galaxy_pairs) == 374
    
def get_all_distances(galaxy_pairs):
    galaxy_sum = 0
    for pair in galaxy_pairs:
        galaxy_sum += get_distance(pair[0], pair[1])
    return galaxy_sum

def test_expand2():
    small_test_data = ["#...", "....", "..#.","...#"]
    assert expand2(small_test_data) == ["#X..", "XXXX", ".X#.",".X.#"]
    
def expand2(data):
    def add_empty2(data):
        new_rows = []
        for row in data:
            if "#" in row:
                new_rows.append(row)
            else:
                new_rows.append(row.replace('.', 'X'))
        return new_rows
    
    replaced_rows = add_empty2(data)
    columns = transpose(replaced_rows)
    replaced_columns = add_empty2(columns)
    new_rows = transpose(replaced_columns)
    return new_rows

def test_galaxies2():
    small_test_data = ["#...", "....", "..#.","...#"]
    test_small = expand2(small_test_data)

    #assert find_galaxies2(expand2(small_test_data)) == [(0,0), (3,3), (4,4)]  
    assert find_galaxies2(expand2(test_data),1) == [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]  
  
def find_galaxies2(data,offset):
    galaxies = []
    
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "#":
                rowmap = data[row][0:col]
                colmap = transpose(data)[col][0:row]
                new_row = colmap.count('X')*(offset) + row
                new_col = rowmap.count('X')*(offset) + col
                galaxies.append((new_row, new_col))
    return galaxies

def test_count2():
    test_part1 = find_galaxies2(expand2(test_data),1)
    test10 = find_galaxies2(expand2(test_data),9)
    test100 = find_galaxies2(expand2(test_data),99)
    assert get_all_distances(get_combinations(test_part1)) == 374
    assert get_all_distances(get_combinations(test10)) == 1030
    assert get_all_distances(get_combinations(test100)) == 8410

input = read_file_lines("day11-input.txt")
if input:
    print('part1', get_all_distances(get_combinations(find_galaxies(expand(input)))))
    print('part2', get_all_distances(get_combinations(find_galaxies2(expand2(input),999999))))
    
    
    