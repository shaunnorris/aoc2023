from aoc2023 import read_file_lines


             #   0123456789  
TEST_DATA =    ['467..114..', # row0
                '...*......', # row1
                '..35..633.', # row2
                '......#...', # row3
                '617*......', # row4
                '.....+.58.', # row5
                '..592.....', # row6
                '......755.', # row7
                '...$.*....', # row8
                '.664.598..'] # row9
  #              012345678  
TEST_DATA2 =   ['467..114.',# row0
                '...*.....',# row1
                '..35..633',# row2
                '......#..',# row3
                '617*.....',# row4
                '.....+.58',# row5
                '..592....',# row6
                '......755',# row7
                '...$.*...',# row8
                '.664.598/']# row9


def test_map_numbers():
    test_mapdata = map_numbers(TEST_DATA)
    assert len(test_mapdata) == 2
    test_numbers, test_symbols = test_mapdata[0], test_mapdata[1]
    assert test_numbers ==[[467, 0, 0], [114, 0, 5], 
                            [35, 2, 2], [633, 2, 6],
                              [617, 4, 0], 
                              [58, 5, 7], 
                              [592, 6, 2], 
                              [755, 7, 6], 
                              [664, 9, 1], [598, 9, 5]] 
    assert test_symbols == [['*', 1, 3], ['#', 3, 6], ['*', 4, 3], ['+', 5, 5], ['$', 8, 3], ['*', 8, 5]]

def test_map2():
    test_mapdata = map_numbers(TEST_DATA2)
    test_numbers, test_symbols = test_mapdata[0], test_mapdata[1]
    assert test_numbers == [[467, 0, 0], [114, 0, 5], 
                            [35, 2, 2], [633, 2, 6],
                              [617, 4, 0], 
                              [58, 5, 7], 
                              [592, 6, 2], 
                              [755, 7, 6], 
                              [664, 9, 1], [598, 9, 5]] 
    assert test_symbols == [['*', 1, 3], ['#', 3, 6], ['*', 4, 3], ['+', 5, 5], ['$', 8, 3], ['*', 8, 5], ['/', 9, 8]]

def map_numbers(data):
    map = {}
    number_list = []
    symbol_list = []
    for row, line in enumerate(data):
        digit_list = []
        coords = []
        for col,char in enumerate(line):
            if char.isdigit():
                if len(digit_list) == 0:
                    coords = [row,col]
                digit_list.append(char)
            else:
                if char != '.':
                    symbol_list.append([char,row,col])
                if len(digit_list) > 0:
                    number = int(''.join(digit_list))
                    number_list.append([number,coords[0],coords[1]])
                    digit_list = []
        if len(digit_list) > 0:
            number = int(''.join(digit_list))
            number_list.append([number,coords[0],coords[1]])
            digit_list = []
    return number_list,symbol_list
                

def test_find_part_numbers():
    test_mapdata = map_numbers(TEST_DATA)
    assert find_part_numbers(test_mapdata) == 4361

def test_find_part_numbers2():
    test_mapdata = map_numbers(TEST_DATA2)
    assert find_part_numbers(test_mapdata) == 4361

                  
def find_part_numbers(mapdata):
    numbers,symbols = mapdata[0],mapdata[1]
    part_numbers = []
    partsum = 0 
    allsum = 0
    for entry in numbers:
        value,row,col = entry[0],entry[1],entry[2]
        start_col = col - 1  
        end_col = col + len(str(value))
        start_row = row - 1
        end_row = row + 1
        part_number = False
        allsum += value
        for i in range(start_row,end_row+1):
            for j in range(start_col,end_col+1):
                for symbol in symbols:
                    x,y  = symbol[1],symbol[2]
                    if x == i and y == j:
                        part_number = True
                    
        if part_number:
            partsum += value
     
    return partsum


def test_get_gear_ratio():
    test_mapdata = map_numbers(TEST_DATA2)
    assert find_gear_ratios(test_mapdata) == 467835

def find_gear_ratios(mapdata):
    numbers,symbols = mapdata[0],mapdata[1]
    stars = {}
    for entry in numbers:
        value,row,col = entry[0],entry[1],entry[2]
        start_col = col - 1  
        end_col = col + len(str(value))
        start_row = row - 1
        end_row = row + 1
        for i in range(start_row,end_row+1):
            for j in range(start_col,end_col+1):
                for symbol in symbols:
                    if symbol[0] == '*':
                        x,y  = symbol[1],symbol[2]
                        if x == i and y == j:
                            if (i,j) not in stars:
                                stars[(i,j)] = [value]
                            else:
                                stars[(i,j)].append(value)
    
    gear_ratio_sum = 0
    for coords,gearlist in stars.items():
        if len(gearlist) == 2:
            ratio = gearlist[0] * gearlist[1]
            gear_ratio_sum += ratio
    return gear_ratio_sum

day3_data = read_file_lines('day3-input.txt')
mapdata = map_numbers(day3_data)
part1 = find_part_numbers(mapdata)
part2 = find_gear_ratios(mapdata)
print('part1',part1)
print('part2',part2)