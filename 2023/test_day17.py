from day17 import Jetstream, Rockpile, Rock, Chamber

def test_rockpile():
    testpile = Rockpile()
   

    expected_shape = {0:[['#','#','#','#']],
                      1:[['.','#','.'],
                         ['#','#','#'],
                         ['.','#','.']],
                      2:[['.','.','#'],
                         ['.','.','#'],
                         ['#','#','#']],
                        3:[['#'],
                             ['#'],
                             ['#'],
                             ['#']],
                        4:[['#','#'],
                             ['#','#']],
                      }
    for rocknum in range(70):
       
        testrock = testpile.nextrock()
        checknum = rocknum % 5
        print("debug", rocknum, checknum)
        print("DEBUG", testrock.shape, expected_shape[checknum])
        assert testrock.shape == expected_shape[checknum], "Rock shape %d is incorrect" % checknum


def test_jetstream():
    expected_jets = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    teststream = Jetstream(expected_jets)
    for x in range(len(expected_jets) + 1000):
        assert teststream.next_jet() == expected_jets[x % len(expected_jets)]

def test_chamber():
    testchamber = Chamber()
    assert len(testchamber.grid) == 3  # Check that the chamber has 3 rows
    for row in testchamber.grid:
        assert row == ['.' for _ in range(7)]  # Check that each row is empty


def test_add_rock():
    testpile = Rockpile()
    testcount = 0
    while testcount < 6:
        print('debug testcount',testcount)
        testrock = testpile.nextrock()
        testchamber = Chamber()
        testchamber.add_rock(testrock)
        testrockheight = (len(testrock.shape))
        testrockwidth = (len(testrock.shape[0]))
        print('debug testrocksize',testrockheight,testrockwidth)
        assert testchamber.grid[-1][2:2+len(testrock.shape[0])] == testrock.shape[0], print(testchamber.grid,testrock.shape)
        testcount +=1   
