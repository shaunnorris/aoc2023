class Rockpile:
    def __init__(self):
        self.rock_counter = 0
        self.rock_shapes = {
            0: [['#','#','#','#']],
            1: [['.','#','.'],
                ['#','#','#'],
                ['.','#','.']],
            2: [['.','.','#'],
                ['.','.','#'],
                ['#','#','#']],
            3: [['#'],
                ['#'],
                ['#'],
                ['#']],
            4: [['#','#'],
                ['#','#']]
        }

    def nextrock(self):
        self.shapenum = self.rock_counter % 5
        self.rock_counter += 1
        return Rock(self.rock_shapes[self.shapenum])
        
    
class Rock:
    def __init__(self, shape):
        self.shape = shape


class Jetstream:
    def __init__(self, input_string):
        self.input_string = input_string
        self.jet_counter = 0

    def next_jet(self):
        direction = self.input_string[self.jet_counter]
        self.jet_counter = (self.jet_counter + 1) % len(self.input_string)
        return direction
    
class Chamber:
    def __init__(self):
        self.grid = []
        self.add_empty_space()

    def add_empty_space(self):
        for _ in range(3):
            self.grid.append(['.' for _ in range(7)])
    
    def add_rock(self, rock):
        for row in reversed(rock.shape):
            new_row = ['.' for _ in range(7)]
            new_row[2:2+len(row)] = row
            self.grid.append(new_row)