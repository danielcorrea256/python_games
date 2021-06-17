import pygame


# VARIABLES
screen_width = 800
screen_height = 600
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
pygame.font.init()


def draw_main_menu():
    win.fill((0,0,0))
    draw_text("Press any key to play", 60, None, None)
    pygame.display.update()


def draw_text(text, size, pos_x, pos_y, color=(255,255,255) ):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)
    
    # The default position to draw text is the middle
    if not pos_x:
        pos_x = top_left_x + (play_width/2) - (label.get_width()/2)

    if not pos_y:
        pos_y = top_left_y + (play_height/2) - (label.get_height()/2)

    win.blit(label, (pos_x, pos_y))



def draw_window(board, score=0, max_score=0):
    win.fill((0,0,0))

    # DRAW THE TITLE
    draw_text("Tetris", 60, None, 30)

    # DRAW THE SCORE
    x = top_left_x + play_width + 40
    y = top_left_y + (play_height/2) + 150
    draw_text("Score: " + str(score), 30, x, y)

    # DRAW THE MAX SCORE
    x = top_left_x - 200
    y = top_left_y + 200
    draw_text("Max_score: " + max_score, 30, x, y)

    # DRAW THE SQUARES OF THE BOARD
    for i_row in range(len(board)):
        for i_column in range(len(board[i_row])):
            x = top_left_x + (i_column * block_size)
            y = top_left_y + (i_row * block_size)
            color = board[i_row][i_column]
            pygame.draw.rect(win, color, (x, y, block_size, block_size),0)

    draw_grid(win, board)
    # DRAW A RED BORDER TO THE BOARD
    pygame.draw.rect(win, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    #pygame.display.update()



# DRAW THE GRID OF THE BOARD
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy+i*block_size), (sx+play_width, sy+i*block_size))
        for j in range(len(grid[i])):
                pygame.draw.line(surface, (128,128,128), (sx + j*block_size, sy), (sx+j*block_size, sy + play_height))



def draw_next_shape(shape):
    x = top_left_x + play_width
    y = top_left_y + (play_height/2)

    draw_text("Next Shape", 30, x + 40, y - 30)

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(win, shape.color, (x+j*block_size+20, y + i*block_size, block_size, block_size), 0)

    #pygame.display.update()