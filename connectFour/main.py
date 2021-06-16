import numpy as np
import pygame
import sys

from Board import Board
from isWinningMove import isWinningMove

# CONSTANTS
ROWS = 6
COLUMNS = 7
SQUARESIZE = 100
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

# INITIALIZE GAME
board = Board(ROWS, COLUMNS)
gameOver = False
playerTurn = 1

pygame.init()

widthScreen = COLUMNS * SQUARESIZE
heightScreen = (ROWS+1) * SQUARESIZE

screenSize = (widthScreen, heightScreen)
screen = pygame.display.set_mode(screenSize)
RADIUS = int(SQUARESIZE/2 - 5) # RADIUS OF CIRCLES IN THE DISPLAY OF THE BOARD
FONT = pygame.font.SysFont("monospace", 50) # THIS IS USED FOR DISPLAY TEXT


# DRAW THE BOARD IN THE DISPLAY
def drawBoard(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMNS):
        for r in range(ROWS):
            if board.pieces[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), heightScreen - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board.pieces[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), heightScreen - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


# AUXILIAR FUNCTION USED TO GET THE COLUMN SELECTED BY CLICK
def getColumn(pos):
    return pos[0] // SQUARESIZE


drawBoard(board)
# *********GAME LOOP************
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # DRAW CIRCLE BY MOUSE MOTION
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, widthScreen, SQUARESIZE))
            posx = event.pos[0]
            col = getColumn(event.pos)
            if playerTurn == 1:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            elif playerTurn == 2:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        # DROP CIRCLE
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, widthScreen, SQUARESIZE))

            col = getColumn(event.pos)  # GET SELECTED COLUMN
            [rowCor, colCor] = board.dropPiece(col, playerTurn)
            #board.printBoard() # print in terminal

            # CHECK IF THE MOVE MAKES 4 IN LINE
            if isWinningMove(board, rowCor, colCor, playerTurn):
                print("Player %d Wins!" % playerTurn)
                colorRGB = RED if playerTurn == 1 else YELLOW
                playerText = "Red" if playerTurn == 1 else "Yellow"
                label = FONT.render("Player %s Wins!!!" % playerText, 1, colorRGB)
                screen.blit(label, (100,20))
                gameOver = True


            drawBoard(board)
            playerTurn = (playerTurn % 2) + 1   # UPDATE TURN

# IF THERE IS A WINNER, WAIT 3000 ms TO EXIT
pygame.time.wait(3000) 