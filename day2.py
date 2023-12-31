from aoc2023 import read_file_lines
import re

test_gameset =['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 
               'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 
               'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 
               'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 
               'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']


def test_parse_game():
    assert parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {'blue': 6, 'green': 2, 'id': 1, 'red': 4}
    assert parse_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")  == {'id': 2, 'blue': 4, 'green': 3, 'red': 1}
    assert parse_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")  == {'id': 3, 'green': 13, 'blue': 6, 'red': 20}
    assert parse_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")  == {'id': 4, 'green': 3, 'red': 14, 'blue': 15}
    assert parse_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")  == {'id': 5, 'red': 6, 'blue': 2, 'green': 3}

def parse_game(game_string):   
    game_cubes = {}
    game_id, cubeinfo = game_string.split(":")
    game_cubes['id'] = int(game_id.split()[-1]) 
    
    separators = ',|;'
    cubes = re.split(separators, cubeinfo)
    for cube in cubes:
        qty, colour = cube.strip().split()
        if colour in game_cubes:
            if game_cubes[colour] < int(qty):
                game_cubes[colour] = int(qty)
        else:
            game_cubes[colour] = int(qty)
    return game_cubes

def test_possibility():
    test_possible_limits = {'blue': 14, 'green': 13, 'red': 12}
    assert possible(test_gameset[0], test_possible_limits) == 1
    assert possible(test_gameset[1], test_possible_limits) == 2
    assert possible(test_gameset[2], test_possible_limits) == 0
    assert possible(test_gameset[3], test_possible_limits) == 0
    assert possible(test_gameset[4], test_possible_limits) == 5
    
def possible(game_string, possible_limits):
    
    game_cubes = parse_game(game_string)
    for colour in game_cubes:
        if colour != 'id':
            if game_cubes[colour] > possible_limits[colour]:
                return 0
    return game_cubes['id']



def test_solve_part1():
    assert solve_part1(test_gameset) == 8

def solve_part1(gamedata):
    possible_sum = 0
    for game in gamedata:
        possible_sum += possible(game, part1_limits)
    return possible_sum



def test_find_power():
    assert find_power(test_gameset[0]) == 48
    assert find_power(test_gameset[1]) == 12
    assert find_power(test_gameset[2]) == 1560
    assert find_power(test_gameset[3]) == 630
    assert find_power(test_gameset[4]) == 36

def find_power(game_string):
    game_cubes = parse_game(game_string)
    power = game_cubes['blue'] * game_cubes['red'] * game_cubes['green']
    return power

def test_solve_part2():
    assert solve_part2(test_gameset) == 2286

def solve_part2(gamedata):   
    total_power = 0
    for game in gamedata:
        total_power += find_power(game)
    return total_power


input = read_file_lines('./input/day2-input.txt')
part1_limits = {'blue': 14, 'green': 13, 'red': 12}
if input:
    print('Part 1:', solve_part1(input))
    print('part 2:', solve_part2(input))