from aoc2023 import read_file_lines

testdata = read_file_lines("./input/day9-test-input.txt")


def test_parse():
    if testdata:
        assert parse(testdata) == [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
    
def parse(datalines):
    series = []
    for line in datalines:
        series.append([int(item) for item in line.strip().split(" ")])
    return series

def test_pyramid():
    if testdata:
        assert pyramid(parse(testdata)[0]) == {0: [0, 3, 6, 9, 12, 15], 1: [3, 3, 3, 3, 3]} 
        assert pyramid(parse(testdata)[1]) == {0: [1, 3, 6, 10, 15, 21], 1: [2, 3, 4, 5, 6], 2: [1, 1, 1, 1]}
        assert pyramid(parse(testdata)[2]) == {0: [10, 13, 16, 21, 30, 45], 1: [3, 3, 5, 9, 15], 2: [0, 2, 4, 6], 3: [2, 2, 2]}
        
def pyramid(series):
    pyramid = {}
    pyramid[0] = series
    solved = False
    while not solved:
        level = max(pyramid) + 1
        oneup = pyramid[level-1]
        newlist = []
        for i in range(1,len(oneup)):
            newlist.append(oneup[i] - oneup[i-1])
        if all(element == 0 for element in newlist):
            solved = True
        else:
            pyramid[level] = newlist
    
    return pyramid
    
def test_solve():
    if testdata:
        assert solve(pyramid(parse(testdata)[0])) == 18
        assert solve(pyramid(parse(testdata)[1])) == 28
        assert solve(pyramid(parse(testdata)[2])) == 68
        
def solve(pyramid):
    levels = max(pyramid)
    for i in range(levels-1,-1,-1):
        pyramid[i].append(pyramid[i][-1] + pyramid[i+1][-1])
    return pyramid[0][-1]

def test_solve_all():
    if testdata:
        assert solve_all(parse(testdata)) == 114
        assert solve_all(parse(testdata),2) == 2

def solve_all(data,part=1):
    grand_total = 0
    for series in data:
        if part == 1:
            grand_total += solve(pyramid(series))
        else:
            grand_total += solve_left(pyramid(series))
    return grand_total

   
def test_solve_left():
    if testdata:
        assert solve_left(pyramid(parse(testdata)[0])) == -3
        assert solve_left(pyramid(parse(testdata)[1])) == 0
        assert solve_left(pyramid(parse(testdata)[2])) == 5
        
def solve_left(pyramid):
    levels = max(pyramid)
    for i in range(levels-1,-1,-1):
        pyramid[i].insert(0,pyramid[i][0] - pyramid[i+1][0])
    return pyramid[0][0]

input = read_file_lines("./input/day9-input.txt")
if input:
    print('part1', solve_all(parse(input)))
    print('part2', solve_all(parse(input),2))