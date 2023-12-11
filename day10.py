from aoc2023 import read_file_lines

test1 = read_file_lines("./input/day10-test-1.txt")
test2 = read_file_lines("./input/day10-test-2.txt")
test3 = read_file_lines("./input/day10-test-3.txt")
test4 = read_file_lines("./input/day10-test-4.txt")

def test_parse():
    if test1:
        assert parse(test1) == [['-', 'L', '|', 'F', '7'], ['7', 'S', '-', '7', '|'], ['L', '|', '7', '|', '|'], ['-', 'L', '-', 'J', '|'], ['L', '|', '-', 'J', 'F']]
    
def parse(datalines):
    series = []
    for line in datalines:
        series.append([item for item in line.strip()])
    return series

def test_find_start():
    if test1:
        assert find_start(parse(test1)) == (1,1)
    
def find_start(series):
    for row in range(len(series)):
        for col in range(len(series[row])):
            if series[row][col] == 'S':
                return (row,col)
            
def test_find_next():
    if test1:
        testmap1 = parse(test1)
        assert find_next(test1,'-', 'E',(1,2)) == ('7','E',(1,3))
        assert find_next(test1,'7','E',(1,3)) == ('|', 'S', (2, 3))
        assert find_next(test1,'|', 'S', (2, 3)) == ('J', 'S', (3, 3))
        assert find_next(test1,'J', 'S', (3, 3)) == ('-', 'W', (3, 2))
        assert find_next(test1,'-', 'W', (3, 2)) == ('L', 'W', (3, 1))
        assert find_next(test1,'L', 'W', (3, 1)) == ('|', 'N', (2, 1))
        assert find_next(test1,'|', 'N', (2, 1)) == ('S', 'N', (1, 1))    
        

def find_next(map,current_pipe,current_direction,current_position):
    PIPE_MAP = {'|': {'N': 'N', 'S': 'S'},
                '-': {'E': 'E', 'W': 'W'},
                'F': {'N': 'E', 'W': 'S'},
                '7': {'N': 'W', 'E': 'S'},
                'J': {'S': 'W', 'E': 'N'},
                'L': {'S': 'E', 'W': 'N'}}
    
    DIRECTION_MAP = {'N': (-1,0), 'S': (1,0), 'E': (0,1), 'W': (0,-1) }
    
    current_row,current_col = current_position[0],current_position[1]
    new_direction = PIPE_MAP[current_pipe][current_direction]
    row_offset,col_offset = DIRECTION_MAP[new_direction]

    new_row,new_col = current_row + row_offset, current_col + col_offset
    new_pipe = map[new_row][new_col]
    return (new_pipe,new_direction,(new_row,new_col))

def test_walk_pipe():
    if test1:
        testmap1 = parse(test1)
        assert walk_pipe(testmap1,(1,1),"E") == 4
    if test2:
        testmap2 = parse(test2)
        assert walk_pipe(testmap2,(2,0),"E") == 8
    
    
def walk_pipe(map,start_position,start_direction):
    pipe_list = []
    current_position = start_position
    pipe_list.append('S')
    if start_direction in ["N","S"]:
        current_pipe = '|'
    elif start_direction in ["E","W"]:
        current_pipe = '-'
    current_direction = start_direction
    while current_pipe != 'S':
        current_pipe,current_direction,current_position = find_next(map,current_pipe,current_direction,current_position)
        pipe_list.append(current_pipe)
    return len(pipe_list) // 2

def test_pipe_coords():
    if test1:
        testmap1 = parse(test1)
        assert pipe_coords(testmap1,(1,1),"E") == [(1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1)]
    if test3:
        testmap3 = parse(test3)
        assert pipe_coords(testmap3,(1,1),'E') == [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (7, 6), (6, 6), (5, 6), (5, 7), (5, 8), (4, 8), (3, 8), (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]

def pipe_coords(map,start_position,start_direction):
    pipe_list = []
    current_position = start_position
    if start_direction in ["N","S"]:
        current_pipe = '|'
    elif start_direction in ["E","W"]:
        current_pipe = '-'
    current_direction = start_direction
    while current_pipe != 'S':
        current_pipe,current_direction,current_position = find_next(map,current_pipe,current_direction,current_position)
        pipe_list.append(current_position)
    return pipe_list

def test_inside_loop():
    if test3:
        testmap3 = parse(test3)
        testcoords = pipe_coords(testmap3,(1,1),'E')
        assert inside_loop(6,2,testcoords) == True
        assert inside_loop(6,8,testcoords) == True
        assert inside_loop(4,3,testcoords) == False
        assert inside_loop(5,5,testcoords) == False
    
def inside_loop(x, y, polygon):
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def test_count_inside():
    if test3:
        testmap3 = parse(test3)
        testcoords3 = pipe_coords(testmap3,(1,1),'E')
        assert count_inside(testmap3,testcoords3) == 4
    if test4:
        testmap4 = parse(test4)
        testcoords4 = pipe_coords(testmap4,(4,12),'E')
        assert count_inside(testmap4,testcoords4) == 8
        
def count_inside(map,loop):
    inside_count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if (row,col) not in loop and inside_loop(row,col,loop):
                inside_count += 1
    return inside_count

input = read_file_lines("./input/day10-input.txt")
if input:
    map = parse(input)
    print('part1', walk_pipe(map,find_start(map),'N'))
    print('part2', count_inside(map,pipe_coords(map,find_start(map),'N')))