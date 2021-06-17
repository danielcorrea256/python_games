import pygame

from data import get_max_score, update_max_score
from Board import Board
from Piece import Piece 
from graphics import draw_text, draw_window, draw_main_menu, draw_next_shape


def main():
    # INITIALIZE GAME'S VARIABLES
    game_over = False
    board = Board({})
    change_piece = False
    current_piece = Piece()
    next_piece = Piece()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0
    max_score = get_max_score()

    # ******** GAME LOOP *************
    while not game_over:
        board = Board(board.locked_positions) # THIS IS NECCESARY FOR UPDATE THE BOARD
        
        # ***PIECE FALLING****
        fall_speed = 0.27
        fall_time += clock.get_rawtime()
        clock.tick()
        # EACH SECOND THE PIECE FALL 1 UNIT IN THE Y AXIS
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            # IF THE PIECE HITS THE GROUND
            if not(board.valid_space(current_piece)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        #****KEYBOARD MOVEMENTS******
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (board.valid_space(current_piece)):
                      current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (board.valid_space(current_piece)):
                      current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (board.valid_space(current_piece)):
                      current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (board.valid_space(current_piece)):
                      current_piece.rotation -= 1


        # GET THE POSITION THAT TAKE THE PIECE
        shape_pos = current_piece.convert_shape_format()

        # ADD PIECE TO THE BOARD IN ORDER TO DRAW THE PIECE LATER
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                board.board[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                board.locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = Piece()    # GENERATE NEW RANDOM PIECE
            change_piece = False
            score += board.clear_rows() * 10 # BECAUSE THERE ARE 10 COLUMNS, THEN FOR EACH ROW THERE ARE 10 BLOCKS

        draw_window(board.board, score, max_score)  # DRAW BOARD
        draw_next_shape(next_piece)     # DRAW NEXT PIECE
        pygame.display.update()     # DO THE PREVIOUS DRAWS

        # ******LOST ********+
        if board.check_lost():
            update_max_score(score)     # WRITE max_score.txt IF THE SCORE IS A MAXIMUM SCORE
            draw_text("YOU LOST", 80, None, None)   # TEXT AT CENTER BECAUSE NONE, NONE
            pygame.display.update()
            pygame.time.delay(1500)
            game_over = True


# *********MENU*******
def main_menu():
    run = True
    while run:
        draw_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.display.quit()


# ********* RUN ***********
main_menu()