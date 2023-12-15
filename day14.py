from aoc2023 import read_file_lines, transpose

testgrid = read_file_lines('./input/day14-test-input.txt')

def test_roll_row():
    assert roll_row('OO.O.O..##') == 'OOOO....##'
    assert roll_row('O.#..O.#.#') == 'O.#O...#.#'
    assert roll_row('....O#.O#.') == 'O....#O.#.'
    assert roll_row('#...O#.O#.') == '#O...#O.#.'
    assert roll_row('....#.....') == '....#.....'
    assert roll_row('#####') == '#####'
    assert roll_row('OOOOOOO') == 'OOOOOOO'

    
def roll_row(row):
    if 'O' in row:
        newrow = []
        hashes = [index for index, char in enumerate(row) if char == '#']
        hashes.append(len(row))
        if row[0] != '#':
            hashes.insert(0,0)
        sections = []
        for q in range(len(hashes)-1):
            sections.append(row[hashes[q]:hashes[q+1]])
        for section in sections:
            if section[0] == '#':
                newrow.append('#')   
            newrow.append(section.count('O')*'O')
            newrow.append(section.count('.')*'.')    
        return ''.join(newrow)
    else:
        return row


def test_roll_north():
    if testgrid:
        assert roll_north(testgrid) == ['OOOO.#.O..',
                                        'OO..#....#',
                                        'OO..O##..O',
                                        'O..#.OO...',
                                        '........#.',
                                        '..#....#.#',
                                        '..O..#.O.O',
                                        '..O.......',
                                        '#....###..',
                                        '#....#....']
        
def roll_north(grid):
    tgrid = transpose(grid)
    newgrid = []
    for row in tgrid:
        newgrid.append(roll_row(row))
    return transpose(newgrid)

def test_find_load():
     if testgrid:
        assert find_load(roll_north(testgrid)) == 136
        
def find_load(grid):
    load = 0
    for i, row in enumerate(grid[::-1]):
        load += (i+1)*row.count('O')
    return load

def rotate_clockwise(grid):
    if not grid:
        return []

    # Calculate the dimensions of the original grid
    rows, cols = len(grid), len(grid[0])

    # Transpose the grid
    transposed = [[grid[j][i] for j in range(rows)] for i in range(cols)]

    # Reverse each row to complete the 90-degree clockwise rotation
    rotated_grid = [row[::-1] for row in transposed]

    return rotated_grid

def test_spin_cycle():
    if testgrid:
        assert spin_cycle(testgrid) == 64
        
    
def spin_cycle(grid, runs=1000,target=1000000000):
    current_grid = grid
    loads = []
    allseqs = {}
    load_pattern = {}
    for x in range(1,runs+1):
        for tilt in range(4):
            current_grid = roll_north(current_grid)
            current_grid = rotate_clockwise(current_grid)
            current_load = find_load(current_grid)
        loads.append(current_load)
    pattern_start,found_sequence = find_sequences(loads)
    offset = (target-pattern_start) % len(found_sequence)
    return found_sequence[offset]
    
    
def find_sequences(loads):
    found = []
    for window in range(5,100):
        seen = set()
        for start in range(len(loads)-window):
            testseq = tuple(loads[start:start+window])
            if testseq in seen:
                lastseq = tuple(loads[start-window:start])
                if  lastseq == testseq:
                    found.append((start-window+1,testseq))
                    break
            else:
                seen.add(testseq)
    if len(found) >0:
        return found[-1]
    else:
        return None




input = read_file_lines('./input/day14-input.txt')
if input:
    print('part1', find_load(roll_north(input)))
    print('part2', spin_cycle(input))
    