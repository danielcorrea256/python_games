import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# IMPORT SNAKE CLASS
from Snake import Snake
# IMPORT CUBE OBJECT
from Cube import Cube

# CONSTANTS
width = 500
height = 500
rows = 20


# DRAW GRID
def drawGrid(surface):
    x, y = 0, 0
    colorGrid = (200, 200, 200) # GRAY COLOR
    for i in range(rows):
        x += width // rows
        y += height // rows
        # DRAW HORIZONTAL LINE
        pygame.draw.line(surface, colorGrid, (0, y),(width, y))
        # DRAW VERTICAL LINE
        pygame.draw.line(surface, colorGrid, (x, 0),(x, height))


# UPDATE THE WINDOW WITH THE NEW POS OF THE SNAKE AND THE SNACK
def redrawWindow(surface, snake, snack):
    surface.fill((0,0,0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(surface)
    pygame.display.update()


# GENERATE THE RANDOM SNACK
def randomSnack(item):
    positionSnake = item.body
    # THIS LOOPS ENDS WHEN GENERATES A VALID SNACK
    while True:
        # GENERATE RANDOM COORDINATES
        x = random.randrange(rows)
        y = random.randrange(rows)
        
        # CHECK IF THE RANDOM COORDINATES ARE NOT IN A SNAKE CUBE
        samePosition = filter(lambda z: z.pos == (x, y), positionSnake)
        if len(list(samePosition)) > 0:
            continue
        else:
            break
    
    return (x, y) # RETURN THE COORDINATES


# A MESSAGE BOX
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


# MAIN FUNCTION OF THE GAME
def main():
    s = Snake((10, 10))
    win = pygame.display.set_mode((width, height)) # WINDOW
    clock = pygame.time.Clock()
    snack = Cube(randomSnack(s), color=(0, 255, 0)) # SNACK

    flag = True # FLAG IS THE CONDITION TO KEEP PLAYING

    # ******* GAME LOOP ********
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        # MOVE THE SNAKE
        s.move()

        # IF THE SNAKE HIT THE SNACK
        if s.body[0].pos == snack.pos:
            s.addCube() # ADD A CUBE TO THE SNAKE
            snack = Cube(randomSnack(s), color=(0, 255, 0)) # GENERATE A RANDOM SNACK

        # IF THE SNAKE HIT ITSELF
        for i in range(len(s.body)):
            # GET THE POSITION OF THE CUBES BEHIND THE i CUBE
            cubesBehind = map(lambda z: z.pos, s.body[i+1:])
            if s.body[i].pos in list(cubesBehind):
                message_box("You lost!", "Score: %d" % len(s.body))
                s.reset((10,10))
                break

        # REDRAW THE WINDOW
        redrawWindow(win, s, snack)

main()
