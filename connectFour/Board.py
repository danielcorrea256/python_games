import numpy as np

class Board:
    # A BOARD HAS ROW AND COLUMNS THAT CONTAIN PIECES
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.pieces = np.zeros((rows, columns))


    # PRINT TO CONSOLE
    def printBoard(self):
        print(np.flip(self.pieces, 0))


    # DROP PIECE TO BOARD
    def dropPiece(self, col, piece):
        row = self._getNextOpenRow(col)
        self.pieces[row][col] = piece
        return [row, col]


    # CHECK IF IT IS A VALID LOCATION
    def isValidLocation(self, col):
        try:
            return self.pieces[self.rows-1][col] == 0
        except IndexError:
            return False


    # RETURN THE NEXT OPEN ROW IN A COLUMN
    def _getNextOpenRow(self, col):
        for i in range(self.rows):
            if self.pieces[i][col] == 0:
                return i
