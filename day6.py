from aoc2023 import read_file_lines

testdata = read_file_lines('./input/day6-test-input.txt')

def test_parse_data():             #(time,  distance)
    if testdata:
        assert parse_data(testdata) == [(7, 9), (15, 40), (30, 200)]
    
def parse_data(lines):
    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))
    races = []
    for i, (time, distance) in enumerate(zip(time_values, distance_values), start=1):
        races.append((time, distance))
    return races

def test_run_race():
    assert run_race((7, 9),0) == False
    assert run_race((7, 9),1) == False
    assert run_race((7, 9),2) == True
    assert run_race((7, 9),3) == True
    assert run_race((7, 9),4) == True
    assert run_race((7, 9),5) == True
    assert run_race((7, 9),6) == False
    assert run_race((7, 9),7) == False
    
               
def run_race(race, button_time):
    race_time = race[0]
    race_dist = race[1]
    speed = button_time
    time_left = race_time - button_time
    travelled = speed * time_left
    if travelled > race_dist:
        return True
    else:
        return False     

def test_calc_winners():
    assert calc_winners((7, 9)) == 4
    
def calc_winners(race):
    race_time = race[0]
    winners = 0
    for hold_time in range(0,race_time+1):
        if run_race(race,hold_time):
            winners += 1
    return winners

def test_all_races():
    if testdata:
        racedata = parse_data(testdata)
        assert all_races(racedata) == 288
    
def all_races(racedata):
    product = 1
    for race in racedata:
        product = product * calc_winners(race)
    return product

def test_parse_part2():
    if testdata:
        assert parse_part2(testdata) == (71530,940200)
    
def parse_part2(lines):
    time = int(''.join(filter(str.isdigit, lines[0])))
    distance = int(''.join(filter(str.isdigit, lines[1])))
    return (time,distance)

input = read_file_lines('./input/day6-input.txt')
if input:
    print('part1',all_races(parse_data(input)))
    print('part2',calc_winners(parse_part2(input)))