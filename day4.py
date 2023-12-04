from aoc2023 import read_file_lines
           
def test_parse_line():
    assert parse_cards("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == (1, [41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53])
    assert parse_cards("Card  91: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == (91, [41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53])
    assert parse_cards("Card  1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == (1, [41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53])
    assert parse_cards("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == (2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19])
    assert parse_cards("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == (3, [1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1])
    assert parse_cards("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == (4, [41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83])
    assert parse_cards("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == (5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36])
    assert parse_cards("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == (6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])

def parse_cards(line):
    line = line.replace("  ", " ")
    chunks = line.split(":")
    chunks[0] = chunks[0].replace("Card", "").strip()
    card_number = int(chunks[0])
    cards = chunks[1].split("|")
    cards = [c.strip() for c in cards]
    cards = [c.split(" ") for c in cards]
    cards = [[int(i) for i in c] for c in cards]
    return (card_number, cards[0], cards[1])

def test_parse_game():
    testdata = read_file_lines("day4-test-input.txt")
    if testdata:
        assert len(parse_game(testdata)) == 6
        
def parse_game(data):
    gamelist = []
    for line in data:
        gamelist.append(parse_cards(line))
    return gamelist

def test_score_cards():
    assert score_cards((1, [41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53])) == 8
    assert score_cards((2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19])) == 2
    assert score_cards((3, [1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1])) == 2
    assert score_cards((4, [41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83])) == 1
    assert score_cards((5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36])) == 0
    assert score_cards((6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])) == 0
    

def score_cards(carddata):
    card_number = carddata[0]
    winners = set(carddata[1])
    played = set(carddata[2])
    matches = list(winners.intersection(played))
    if matches:
        score = 2 ** (len(matches)-1)
    else:
        score = 0
    return score

def test_play_game():
    testdata = read_file_lines("day4-test-input.txt")
    if testdata:
        assert play_game(testdata) == 13        

def play_game(gamedata):
    total_score = 0
    for cards in gamedata:
        total_score += score_cards(parse_cards(cards))
    return total_score

def test_score2():
    testdata = read_file_lines("day4-test-input.txt")
    if testdata:
        assert score2(testdata) == 30
        
def score2(carddata):
    game = parse_game(carddata)
    tracker = {}
    for card in game:
        tracker[card[0]] = 1
    for card in game:
        card_number = card[0]
        winners = set(card[1])
        played = set(card[2])
        matches = len(list(winners.intersection(played)))
        for q in range(tracker[card_number]):
            for i in range(card_number+1,min(card_number+matches+1,len(game)+1)):
                tracker[i] += 1
    return sum(tracker.values())

input = read_file_lines("day4-input.txt")
if input:
    part1 = play_game(input)
    print("part1", part1)
    part2 = score2(input)
    print("part2",part2)