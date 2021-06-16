def isWinningMove(board, row, col, piece):
    # THE FUNCTION CHECKS IF THERE IS 4 PIECES IN A ROW IN DIFFERENT WAYS
    # ALWAYS THERE IS A COUNTER THAT COUNTS THE PIECES IN ROW 


    # CHECK IF THERE IS 4 HORIZONTAL PIECES IN ROW
    def _horizontal():
        
        counterPieces = 1

        pointerCol = col
        # COUNT THE PIECES TO LEFT
        while (pointerCol - 1) >= 0 and board.pieces[row][pointerCol-1] == piece:
            counterPieces += 1
            pointerCol -= 1

        pointerCol = col
        # COUNT THE PIECES TO RIGHT
        while (pointerCol + 1) <= board.columns - 1 and board.pieces[row][pointerCol+1] == piece:
            counterPieces += 1
            pointerCol += 1

        return counterPieces >= 4



    # CHECK IF THERE IS 4 VERTICAL PIECES IN ROW
    def _vertical():
        counterPieces = 1

        pointerRow = row
        # COUNT THE PIECES TO BELOW
        while(pointerRow - 1) >= 0 and board.pieces[pointerRow-1][col] == piece:
            counterPieces += 1
            pointerRow -= 1

        pointerRow = row
        # COUNT THE PIECES TO ABOVE
        while(pointerRow + 1) <= board.rows - 1 and board.pieces[pointerRow+1][col] == piece:
            counterPieces += 1
            pointerRow +=1

        return counterPieces >= 4



    # CHECK IF THERE IS 4 PIECES IN ROW IN DIAGONAL UP
    def _diagonalUp():
        counterPieces = 1

        pointerRow = row
        pointerCol = col
        # COUNT THE PIECES TO BELOW-LEFT IN DIAGONAL
        while (pointerRow-1) >= 0 and (pointerCol-1) >= 0 and board.pieces[pointerRow-1][pointerCol-1] == piece:
            counterPieces += 1
            pointerRow -= 1
            pointerCol -= 1

        pointerRow = row
        pointerCol = col
        # COUNT THE PIECES TO ABOVE-RIGHT IN DIAGONAL
        while (pointerCol+1) <= (board.columns-1) and (pointerRow+1) <= (board.rows-1) and board.pieces[pointerRow+1][pointerCol+1] == piece:
            counterPieces += 1
            pointerRow += 1
            pointerCol += 1

        return counterPieces >=4



    # CHECK IF THERE IS 4 PIECES IN ROW IN DIAGONAL DOWN
    def _diagonalDown():
        counterPieces = 1

        pointerRow = row
        pointerCol = col
        # COUNT THE PIECES TO BELOW-RIGHT IN DIAGONAL
        while (pointerRow-1) >= 0 and (pointerCol+1) <= (board.columns-1) and board.pieces[pointerRow-1][pointerCol+1] == piece:
            counterPieces += 1
            pointerRow -= 1
            pointerCol += 1

        pointerRow = row
        pointerCol = col
        # COUNT THE PIECES TO ABOVE-LEFT IN DIAGONAL
        while (pointerRow+1) <= (board.rows-1) and (pointerCol-1) >= 0 and board.pieces[pointerRow+1][pointerCol-1] == piece:
            counterPieces += 1
            pointerRow += 1
            pointerCol -= 1

        return counterPieces >= 4

    # CHECK IF THERE IS 4 PIECES OR MORE IN ROW IN HORIZONTAL, VERTICAL OR DIAGONAL
    return _horizontal() or _vertical() or _diagonalUp() or _diagonalDown()
