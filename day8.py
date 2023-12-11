from aoc2023 import read_file_lines
import math

testinput = read_file_lines("./input/day8-test-input.txt")
testinput2 = read_file_lines("./input/day8-test2-input.txt")

def test_parse():
    if testinput:
        assert len(testinput) == 9
        test_desert = parse(testinput)
        assert test_desert['ins'] == "RL"
        assert test_desert['nodes'] == {'AAA': ('BBB', 'CCC'), 
                                        'BBB': ('DDD', 'EEE'), 
                                        'CCC': ('ZZZ', 'GGG'), 
                                        'DDD': ('DDD', 'DDD'), 
                                        'EEE': ('EEE', 'EEE'), 
                                        'GGG': ('GGG', 'GGG'), 
                                        'ZZZ': ('ZZZ', 'ZZZ')}

def parse(lines):
    ins = lines[0]
    nodes = {}
    for i in range(2,len(lines)):
        key,left,right = lines[i][0:3],lines[i][7:10],lines[i][12:15]
        nodes[key] = (left,right)
    return {'ins':ins,'nodes':nodes}

def test_walk():
    if testinput:
        test_desert = parse(testinput)
        assert walk(test_desert,'AAA','ZZZ') == 2
    
    
def walk(desert,start,finish):
    ins = desert['ins']
    nodes = desert['nodes']
    steps = 0
    done = False
    current = start
    while not done:
        turn = ins[steps % len(ins)]
        if current == finish:
            done = True
        else:
            left,right = nodes[current]
            if turn == 'L':
                current = nodes[current][0]
            elif turn == 'R':
                current = nodes[current][1]
            else:
                break
            steps += 1
           
    return steps

def test_get_starts():
    if testinput2:
        test_desert = parse(testinput2)
        assert get_starts(test_desert) == ['11A','22A']

def get_starts(desert):
    start_keys = []
    for key in desert['nodes'].keys():
        if key[2] == 'A':
            start_keys.append(key) 
    return start_keys

def test_ghost_cycle():
    if testinput2:
        test_desert = parse(testinput2)
        assert ghost_cycle(test_desert,('22A')) == 3
        assert ghost_cycle(test_desert,('11A')) == 2

def ghost_cycle(desert,start):
    ins = desert['ins']
    nodes = desert['nodes']
    zeds = []
    done = False
    current = start
    steps = 0
    while not done:
        turn = ins[steps % len(ins)]
        if len(zeds) == 3:
            done = True
        else:
            left,right = nodes[current]
            if turn == 'L':
                current = nodes[current][0]
            elif turn == 'R':
                current = nodes[current][1]
            else:
                break
        if current[2] == 'Z':
            zeds.append(steps)
        steps += 1
    return zeds[2] - zeds[1]


def test_ghost_walk():
    if testinput2:
        test_desert = parse(testinput2)
        assert ghost_walk(test_desert,('11A','22A')) == 6

def ghost_walk(desert,starts):
    cycles = []
    for start in starts:
        cycles.append(ghost_cycle(desert,start))
    return math.lcm(*cycles)


input = read_file_lines("./input/day8-input.txt")
if input:
    desert = parse(input)
    starts = get_starts(desert)
    print('part 1:',walk(desert,'AAA','ZZZ'))
    print('part 2:',ghost_walk(desert,starts))

