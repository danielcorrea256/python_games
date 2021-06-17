class Board:
    def __init__(self, locked_positions={},n_rows=20, n_columns=10):
        self.locked_positions = locked_positions
        self.board = self.create_board(locked_positions, n_rows, n_columns)
        self.n_rows = n_rows
        self.n_columns = n_columns


    # CREATE A BOARD AS AN 2 DIMENSIONAL ARRAY
    def create_board(self, locked_positions={}, n_rows=20, n_columns=10):
        # Create a 2 dimensional array
        board = [[(0,0,0) for _ in range(n_columns)] for _ in range(n_rows)]

        # Plug in the locked positions in the new board
        for i in range(n_rows):
            for j in range(n_columns):
                if (j, i) in locked_positions:
                    x = locked_positions[(j, i)]
                    board[i][j] = x

        return board


    # CHECK IF A SHAPE IS IN A VALID SPACE
    def valid_space(self, shape):
        accepted_pos = [[(j, i) for j in range(10) if self.board[i][j] == (0,0,0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = shape.convert_shape_format()
        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True



    # CHECK IF THE PLAYER LOST
    # CHECK IF A PIECE IS ABOVE THE LIMIT Y
    def check_lost(self):
        for pos in self.locked_positions:
            x, y = pos
            if y < 1:
                return True
        return False



    # CLEAR ROWS WHEN A ROW IS FULL
    def clear_rows(self):
        inc = 0
        for i in range(len(self.board)-1, -1, -1):
            row = self.board[i]
            if (0,0,0) not in row:  # CHECK IF THERE IS NONE BLACK SQUARE
                inc += 1
                ind = i 
                for j in range(len(row)):
                    try:
                        del self.locked_positions[(j,i)]
                    except:
                        continue

        # SHIFT ROWS TO BELOW
        if inc > 0:
            for key in sorted(list(self.locked_positions), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    self.locked_positions[newKey] = self.locked_positions.pop(key)
        
        return inc



