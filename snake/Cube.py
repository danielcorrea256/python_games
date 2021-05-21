import pygame

# IMPORTANT CONSTANTS
width = 500
rows = 20

class Cube:
    def __init__(self, position, dirx = 1, diry = 0, color=(255, 0, 0)):
        self.pos = position
        self.dirx = dirx
        self.diry = diry
        self.color = color


    def move(self, new_dirx, new_diry):
        self.dirx, self.diry = new_dirx, new_diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)


    def draw(self, surface, eyes=False):
        # DIS IS THE DISTANCE BETWEEN ROWS
        dis = width // rows # KEEP IN MIND THAT THE WINDOW IS A SQUARE, WIDTH x WIDTH = WIDTH x HEIGHT
        [i, j] = self.pos

        # DRAW IN THE WINDOW(surface)
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2)) # +1 or -2 is for an appropiate fit

        # DRAW EYES IF REQUIRED
        if eyes:
            center = dis // 2
            radius = 3
            circleMiddle = (i * dis + center - radius, j*dis+8)
            circleMiddle2 = (i * dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
