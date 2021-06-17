import random

# SHAPE FORMATS

S = [['.....',
    '......',
    '..00..',
    '.00...',
    '.....'],
     ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....']]

Z = [['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
     ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....']]

I = [['..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
     ['.....',
    '0000.',
    '.....',
    '.....',
    '.....']]

O = [['.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]

J = [['.....',
    '.0...',
    '.000.',
    '.....',
    '.....'],
     ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
     ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
     ['.....',
    '..0..',
    '..0..',
    '.00..',
    '.....']]

L = [['.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
     ['.....',
    '..0..',
    '..0..',
    '..00.',
    '.....'],
     ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
     ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]

T = [['.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
     ['.....',
    '..0..',
    '..00.',
    '..0..',
    '.....'],
     ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
     ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]


shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self, x=5, y=0):
        self.x = x  # THE DEFAULT POSITION IS AT THE CENTER
        self.y = y
        self.shape = random.choice(shapes)  # GENERATE A RANDOM CHOICE
        self.color = shape_colors[shapes.index(self.shape)] 
        self.rotation = 0
    

    # RETURN THE POSITIONS THAT THE PIECE TAKES
    def convert_shape_format(self):
        positions = []
        format = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    positions.append((self.x + j, self.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions


