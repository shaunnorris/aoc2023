from aoc2023 import read_file_lines

testdata = read_file_lines('day7-test-input.txt')

def test_parse():
    assert parse(testdata) == [{'hand': '32T3K', 'bid': 765}, 
                               {'hand': 'QQQJA', 'bid': 483}, 
                               {'hand': 'KK677', 'bid': 28}, 
                               {'hand': 'T55J5', 'bid': 684}, 
                               {'hand': 'KTJJT', 'bid': 220}]

def parse(lines):
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append({"hand": hand, "bid": int(bid) })
    return hands

def test_find_type():
    assert find_type("11111") == 6
    assert find_type("5555K") == 5
    assert find_type("JJJKK") == 4
    assert find_type("AAA98") == 3
    assert find_type("11223") == 2
    assert find_type("QQ123") == 1
    assert find_type("AKQJ9") == 0
    
def find_type(hand):
    #6: Five of a kind, where all five cards have the same label: AAAAA
    #5: Four of a kind, where four cards have the same label 
    #4: Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    #3: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    #2: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    #1: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    #0: High card, where all cards' labels are distinct: 23456
    unique = set(hand)
    uc = len(unique)
    max_single = 1
    for card in unique:
        if hand.count(card) > max_single:
            max_single = hand.count(card)   
    if uc == 1:
        return 6
    elif uc == 2:
        if max_single == 4:
            return 5
        elif max_single == 3:
            return 4
    elif uc == 3:
        if max_single == 3:
            return 3
        elif max_single == 2:
            return 2
    elif uc == 4:
        return 1
    elif uc == 5:
        return 0

    
def test_get_card_value():
    assert get_card_value("A") == 14
    assert get_card_value("K") == 13
    assert get_card_value("Q") == 12
    assert get_card_value("J") == 11    
    assert get_card_value("T") == 10
    assert get_card_value("9") == 9
    assert get_card_value("8") == 8
    assert get_card_value("2") == 2
    
def get_card_value(card):
    letter_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    if card.isdigit():
        return int(card)
    else:
        return letter_values[card]
    
def test_compare_hands():
    assert compare_hands("11111", "2222A") == ("11111")
    assert compare_hands("11111","22222") == ("22222")
    assert compare_hands("12345","1234A") == ("1234A")
    assert compare_hands("1234A","12345") == ("1234A")
    assert compare_hands("33322","AAAKK") == ("AAAKK")
    assert compare_hands("AKAKA","1K1K1") == ("AKAKA")
    
def compare_hands(hand1, hand2):
    #compare hands and return the winning hand
    #if hands are equal, return None
    #if hand1 is better, return hand1
    #if hand2 is better, return hand2
    t1 = find_type(hand1)
    t2 = find_type(hand2)
    if t1 > t2:
        return hand1
    elif t1 == t2:
        equal_value = True
        for i in range(0,5):
            c1 = get_card_value(hand1[i])
            c2 = get_card_value(hand2[i])
            if c1 > c2:
                return hand1
            elif c2 > c1:
                return hand2
    elif t2 > t1:
        return hand2
    
def test_sort_cards():
    testhands = parse(testdata)
    assert sort_cards(testhands) == [{'hand': '32T3K', 'bid': 765, 'rank': 1}, 
                                     {'hand': 'KTJJT', 'bid': 220, 'rank': 2}, 
                                     {'hand': 'KK677', 'bid': 28, 'rank': 3}, 
                                     {'hand': 'T55J5', 'bid': 684, 'rank': 4}, 
                                     {'hand': 'QQQJA', 'bid': 483, 'rank': 5}]
    
def sort_cards(hands):
    print(hands)
    for a in range(0,len(hands)):
        print(hands[a]['hand'])
        for b in range(a+1,len(hands)):
            if compare_hands(hands[a]['hand'],hands[b]['hand']) == hands[a]['hand']:
                hands[a], hands[b] = hands[b], hands[a]
    for i in range(0,len(hands)):
        hands[i]['rank'] = i+1  
    print('sorted',hands)
    return hands

def test_winnings():
    sorted_testcards =sort_cards(parse(testdata))
    assert winnings(sorted_testcards) == 6440
    
def winnings(hands):
    winnings = 0
    for hand in hands:
        winnings += hand['bid'] * hand['rank']
    return winnings

input = read_file_lines('day7-input.txt')
if input:
    part1 = winnings(sort_cards(parse(input)))
    print('part1',part1)