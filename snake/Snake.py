import pygame
from Cube import Cube

# IMPORTANT CONSTANTS
WIDTH = 500
ROWS = 20

# SNAKE OBJECT
class Snake:
    def __init__(self, pos, color=(4, 92, 5)):
        self.color = color
        self.head = Cube(pos) 
        self.body = [ self.head ]   # BODY OF THE SNAKE, A LIST OF CUBES
        self.turns = {}     # USED FOR SAVE THE TURNS
        self.dirx = 0   # DIRECTION IN X AXIS
        self.diry = 1   # DIRECTION IN Y AXIS


    def move(self):
        for event in pygame.event.get():
            #if event == pygame.QUIT:
             #   pygame.quit()

            keys = pygame.key.get_pressed()
            # CHOOSE THE DIRECTION BECAUSE THE KEY PRESSED
            # TAKE OPPOSITE DIRECTIONS IS NOT ALLOWED
            if keys[pygame.K_LEFT]:
                self.dirx = -1 if self.dirx == 0 else self.dirx
                self.diry = 0 if self.diry != 0 else self.diry

            elif keys[pygame.K_RIGHT]:
                self.dirx = 1 if self.dirx == 0 else self.dirx
                self.diry = 0 if self.diry != 0 else self.diry

            elif keys[pygame.K_UP]:
                self.dirx = 0 if self.dirx != 0 else self.dirx
                self.diry = -1 if self.diry == 0 else self.diry

            elif keys[pygame.K_DOWN]:
                self.dirx = 0 if self.dirx != 0 else self.dirx
                self.diry = 1 if self.diry == 0 else self.diry

            # SAVE THE POSITION OF THE CUBE WHERE THERE IS A TURN
            # AND THE DIRECTION OF THE TURN
            self.turns[self.head.pos[:]] = [self.dirx, self.diry]


        for index, cube in enumerate(self.body):
            pos = cube.pos[:]
            # CHECK IF THE CUBE SHOULD TURN
            if pos in self.turns:
                turn = self.turns[pos]
                cube.move(turn[0],turn[1])
                if index == len(self.body)-1:
                    self.turns.pop(pos)
            else:
                # IF THE SNAKE ESCAPE OF THE BORDERS
                if cube.dirx == -1 and cube.pos[0] <= 0: 
                    cube.pos = (ROWS-1, cube.pos[1])
                elif cube.dirx == 1 and cube.pos[0] >= ROWS - 1: 
                    cube.pos = (0,cube.pos[1])
                elif cube.diry == 1 and cube.pos[1] >= ROWS - 1: 
                    cube.pos = (cube.pos[0], 0)
                elif cube.diry == -1 and cube.pos[1] <= 0: 
                    cube.pos = (cube.pos[0],ROWS-1)
                # KEEP THE DIRECTION    
                else: 
                    cube.move(cube.dirx,cube.diry)


    # DRAW THE SNAKE(THE CUBES OF THE BODY)
    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True) # DRAW EYES
            else:
                cube.draw(surface)

    
    # THIS IS USED WHEN THE SNAKE EATS A SNACK
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        # THE POSITION OF THE NEW CUBE IS ACCORDING TO THE DIRECTION OF THE TAIL
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))
      
        # SAVE THE DIRECTION OF THE OLD TAIL TO THE NEW TAIL, THE NEW CUBE
        self.body[-1].dirx = dx
        self.body[-1].diry = dy


    # RESET VALUES TO DEFAULT/INITIAL GAME
    def reset(self,pos):
        self.head = Cube(pos)
        self.body = [ self.head ]
        self.turns = {}
        self.dirx = 0
        self.diry = 1

