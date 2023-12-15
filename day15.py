from aoc2023 import read_file_lines

testdata = read_file_lines('./input/day15-test-input.txt')

def test_parse():
    if testdata:
        assert parse(testdata) == ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]
        
def parse(data):
    parsed = []
    dataline = ''.join(data)
    return dataline.split(',')

def test_HASH_algo():
    assert HASH_algo('HASH') == 52
    
def HASH_algo(string):
    #Determine the ASCII code for the current character of the string.
    #Increase the current value by the ASCII code you just determined.
    #Set the current value to itself multiplied by 17.
    #Set the current value to the remainder of dividing itself by 256.
    
    val = 0
    for char in string:
        val += ord(char)
        val = val * 17
        val = val % 256
    return val

def test_analyze():
    assert analyze(["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]) == 1320
    
def analyze(commands):
    total = 0
    for command in commands:
        total += HASH_algo(command)
    return total

def test_arrange_lenses():
    assert arrange_lenses(["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]) == 145
    
def arrange_lenses(commands):
    boxes = {}
        
    for command in commands:
        if command[-1].isdigit():
            operation = command[-2]
            focal_length = int(command[-1])
            label = command[:-2]
        else:
            operation = command[-1]
            label = command[:-1]
        box = HASH_algo(label)
        if box not in boxes:
            boxes[box] = {}
            
        if operation == '-':
            if label in boxes[box].keys():
                del boxes[box][label]
        elif operation == '=':
                boxes[box][label] = focal_length
    total = 0
    for boxnum,boxcontents in boxes.items(): 
        if len(boxcontents) > 0:
            for index, value in enumerate(boxcontents.items()):
                total+= (boxnum+1) * (index+1) * value[1]
            
    return total



input = read_file_lines('./input/day15-input.txt')
if input:
    print('part1', analyze(parse(input)))
    print('part2', arrange_lenses(parse(input)))
   