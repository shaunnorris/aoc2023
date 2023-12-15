from aoc2023 import read_file_lines, transpose

testdata = read_file_lines('./input/day13-test-input.txt')

def test_parse():
    assert parse(testdata) == [['..##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.'], 
                               ['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']]
    
def parse(lines):
    puzzles = [[]]
    for line in lines:
        if line == '':
            puzzles.append([])
        else:
            puzzles[-1].append(line)
    return puzzles

def test_binary_from_row():
    assert binary_from_row('..##..#.') == 50

def binary_from_row(row):
    row = row.replace('.','0')
    row = row.replace('#','1')
    return int(row,2)


def test_get_row_values():
    if testdata:
        assert get_row_values(parse(testdata)[0]) == [102, 90, 385, 385, 90, 102, 346]
        assert get_row_values(parse(testdata)[1]) == [281, 265, 103, 502, 502, 103, 265]
        assert get_row_values(transpose(parse(testdata)[0])) ==  [25, 24, 103, 66, 37, 37, 66, 103, 24] 

def get_row_values(puzzle):
    row_values = []
    for row in puzzle:
        row_values.append(binary_from_row(row))
    return row_values       


def test_find_reflection():
    assert find_reflection([102, 90, 385, 385, 90, 102, 346]) == False 
    assert find_reflection([281, 265, 103, 502, 502, 103, 265]) == 4
    assert find_reflection([25, 24, 103, 66, 37, 37, 66, 103, 24] ) == 5
    
    
def find_reflection(row):
    for i in range(1,len(row)):
        left = row[:i]
        right = row[i:]
        left = left[::-1]
        minlength = min(len(left),len(right))
        
        if left[:minlength] == right[:minlength]:
            print('found reflection at',i)
            return i
    return False
   
def test_analyze_puzzles():
    assert analyze_puzzles(parse(testdata)) == 405
    
def analyze_puzzles(puzzles):
    total = 0
    for puzzle in puzzles:
        guessr = find_reflection(get_row_values(puzzle))
        guessc = find_reflection(get_row_values(transpose(puzzle)))
        print('rows',get_row_values(puzzle))
        print('cols',get_row_values(transpose(puzzle)))
        
      # rows
        if guessr:
            print('reflection found row-wise',guessr * 100)
            total += guessr * 100
        elif guessc:
            print('reflection found col-wise',guessc)
            total += guessc   
        else:
            print('no reflection found')         
        
    return total
        
        

input = read_file_lines('./input/day13-input.txt')
if input: 
    print('part1', analyze_puzzles(parse(input)))       
    
