from aoc2023 import read_file_lines

testdata = read_file_lines("./input/day5-test-input.txt")

def test_read_data():
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

    

input  = read_file_lines("./input/day5-input.txt")
if input:
    part1 = almanac_walk(input)
    print('part1',part1) 

    