from aoc2023 import read_file_lines
from tqdm import tqdm

def test_read_data():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        assert len(testdata) == 33
        assert parse_data(testdata) == {'seed': [79, 14, 55, 13], 
                                        'seed-to-soil map': [[50, 98, 2], [52, 50, 48]], 
                                        'soil-to-fertilizer map': [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 
                                        'fertilizer-to-water map': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], 
                                        'water-to-light map': [[88, 18, 7], [18, 25, 70]], 
                                        'light-to-temperature map': [[45, 77, 23], [81, 45, 19], [68, 64, 13]], 
                                        'temperature-to-humidity map': [[0, 69, 1], [1, 0, 69]], 
                                        'humidity-to-location map': [[60, 56, 37], [56, 93, 4]]}    

def parse_data(data):
    mydata = {}
    for line in data:
        line = line.strip()
        if line:
            title_present = ':' in line
            if title_present:
                titles = line.split(":")
                newkey = titles[0]
                if newkey == 'seeds':
                    mydata['seed'] = []
                    seednums = titles[1].strip().split(" ")
                    seednums = [int(item) for item in seednums]
                    mydata['seed'] = seednums
                else:
                    mydata[newkey] = []
            else:
                mapnums = line.split(" ")
                if mapnums:
                    mapnums = [int(item) for item in mapnums]
                    mydata[newkey].append(mapnums)
    return mydata    
                
def test_from_to_map():
    assert from_to_map(79,[[50, 98, 2], [52, 50, 48]]) == 81
    assert from_to_map(14,[[50, 98, 2], [52, 50, 48]]) == 14
    assert from_to_map(55,[[50, 98, 2], [52, 50, 48]]) == 57
    assert from_to_map(13,[[50, 98, 2], [52, 50, 48]]) == 13
    
def from_to_map(seed, maplist):
    for map in maplist:
        tar,src,spread = map[0],map[1],map[2]
        srchigh = src + spread
        diff = src-tar
        if seed >= src and seed <= srchigh:
            return seed - diff
    return seed

def test_almanac_walk():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        assert almanac_walk(testdata) == 35
        
def almanac_walk(data,partnum=1):
    mydata = parse_data(data)
    pointer = 'seed'
    current_vals = mydata['seed']
    next_ptr = ''
   
    while pointer != 'location':
        current_map = next((key for key in mydata if pointer+'-' in key), None)
        next_ptr = current_map.split('-')[2].split(' ')[0]
        if current_map:
            new_vals = []
            for seed in current_vals:
                new_vals.append(from_to_map(seed,mydata[current_map]))
        pointer = next_ptr
        current_vals = new_vals    
    return min(current_vals)

        
def test_reverse_map():
    assert reverse_map(60, [[60, 56, 37], [56, 93, 4]]) == 56
    assert reverse_map(82, [[60, 56, 37], [56, 93, 4]]) == 78
    assert reverse_map(78,  [[45, 77, 23], [81, 45, 19], [68, 64, 13]]) == 74

        
def reverse_map(seed, maplist):
    for map in maplist:
        tar,src,spread = map[1],map[0],map[2]
        srchigh = src + spread
        diff = src-tar
        if seed >= src and seed <= srchigh:
            return seed - diff
    return seed

def test_reverse_walk():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        assert reverse_walk(testdata,82) == 79
    
def reverse_walk(data,location):
    mydata = parse_data(data)
    pointer = 'location'
    current = location
    next_ptr = ''
   
    while pointer != 'seed':
        current_map = next((key for key in mydata if '-'+pointer in key), None)
        next_ptr = current_map.split('-')[0]
        new_val= reverse_map(current,mydata[current_map])
        print('debug',pointer,next_ptr,current, new_val, mydata[current_map])
        pointer = next_ptr
        current = new_val    
        print('---')
    return current



def test_calc_range():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        parsed_data=parse_data(testdata)
        assert calc_range(parsed_data['humidity-to-location map']) == ([[60, 96, 4], [56, 59, -37]], [[56, 92, 4], [93, 96, -37]])
    
def test_all_ranges():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        parsed_data=parse_data(testdata)
        assert all_ranges(parsed_data) == {'seed-to-soil map': ([[50, 51, -48], [52, 99, 2]], [[98, 99, -48], [50, 97, 2]]), 
                                           'soil-to-fertilizer map': ([[0, 36, -15], [37, 38, -15], [39, 53, 39]], [[15, 51, -15], [52, 53, -15], [0, 14, 39]]), 
                                           'fertilizer-to-water map': ([[49, 56, -4], [0, 41, -11], [42, 48, 42], [57, 60, 50]], [[53, 60, -4], [11, 52, -11], [0, 6, 42], [7, 10, 50]]), 
                                           'water-to-light map': ([[88, 94, 70], [18, 87, -7]], [[18, 24, 70], [25, 94, -7]]), 
                                           'light-to-temperature map': ([[45, 67, -32], [81, 99, 36], [68, 80, 4]], [[77, 99, -32], [45, 63, 36], [64, 76, 4]]), 
                                           'temperature-to-humidity map': ([[0, 0, -69], [1, 69, 1]], [[69, 69, -69], [0, 68, 1]]), 
                                           'humidity-to-location map': ([[60, 96, 4], [56, 59, -37]], [[56, 92, 4], [93, 96, -37]])}


def all_ranges(mydata):
    ranges = {}
    for key in mydata:
        if key != 'seed':
            ranges[key] = calc_range(mydata[key])
    return ranges



def calc_range(maplist):
    end_ranges = []
    start_ranges = []
    for map in maplist:
        end,start,spread = map[0],map[1],map[2]
        operation = end-start
        end_ranges.append([end,end+spread-1,operation])
        start_ranges.append([start,start+spread-1,operation])
    return end_ranges,start_ranges

def test_range_overlap():
    assert range_overlap([[56, 92],[93, 96]],[[0, 0],[1, 69]]) == [[56, 69]]
    assert range_overlap([[77, 99],[45, 63],[64, 76]],[[88, 94],[18, 87]]) ==  [[88, 94], [77, 87], [45, 63], [64, 76]]
    
def range_overlap(set1,set2):  
    overlapping_ranges = []
    
    for range2 in set2:
        for range1 in set1:
            # Find the maximum of the start points
            start_point = max(range1[0], range2[0])
            # Find the minimum of the end points
            end_point = min(range1[1], range2[1])
            operation = range2[2]
            # Check if there is an overlap
            if start_point < end_point:
                overlapping_ranges.append([start_point, end_point,range2[2]])
    
    return overlapping_ranges

def test_range_walk():
    testdata = read_file_lines("day5-test-input.txt")
    if testdata:
        parsed_data=parse_data(testdata)
        assert range_walk(parsed_data) == 82
        
def range_walk(mydata):
   pass
    
    
"""
input  = read_file_lines("day5-input.txt")
if input:
    part1 = almanac_walk(input)
    print('part1',part1) 
""" 
    