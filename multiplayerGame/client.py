import pygame
from network import Network
import pickle

pygame.font.init()
width = 700
height = 700

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        label = font.render(self.text, 1, (255,255,255))
        win.blit(label,
            (self.x + (round(self.width/2)- round(label.get_width()/2)),
            (self.y + (round(self.height/2)- round(label.get_height()/2) ) ))
            )

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False




def redraw_window(win, game, p):
    win.fill((90,90,90))
    pass

    if not game.connected():
        font = pygame.font.SysFont("comicsans", 80)
        label = font.render("Waiting for player ...", 1, (255, 0, 0), True)
        win.blit(label, (width/2-label.get_width()/2, height/2-label.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        label = font.render("Your move", 1, (0, 255, 255))
        win.blit(label, (80, 200))

        font = pygame.font.SysFont("comicsans", 60)
        label = font.render("Opponents", 1, (0, 255, 255))
        win.blit(label, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            label_1 = font.render(move1, 1, (0,0,0))
            label_2 = font.render(move2, 1, (0,0,0))
        else:
            if game.p1Went and p == 0:
                label_1 = font.render(move1, 1, (0,0,0))
            elif game.p1Went:
                label_1 = font.render("Locked In", 1, (0,0,0))
            else:
                label_1 = font.render("Waiting ...", 1, (0,0,0))

            
            if game.p2Went and p == 1:
                label_2 = font.render(move2, 1, (0,0,0))
            elif game.p2Went:
                label_2 = font.render("Locked In", 1, (0,0,0))
            else:
                label_2 = font.render("Waiting ...", 1, (0,0,0))

        if p == 1:
            win.blit(label_2, (100, 350))
            win.blit(label_1, (400, 350))
        else:
            win.blit(label_1, (100, 350))
            win.blit(label_2, (400, 350))    


        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [
    Button("Rock", 50, 500, (0,0,0)), 
    Button("Scissors", 250, 500, (255, 0, 0)),
    Button("Paper", 450, 500, (0, 255, 0))
    ]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()

    player = int(n.get_p())
    print("You are player", player)

    while run:
        clock.tick(60)

        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get into a game")
            break
        
        if game.bothWent():
            redraw_window(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                label = font.render("You Won!", 1, (255, 0, 0))
            elif game.winner() == -1:
                label = font.render("Tie Game!", 1, (255, 0, 0))
            else:
                label = font.render("You lost", 1, (255, 0, 0))

            win.blit(label, 
                (width/2 - (label.get_width()/2), height/2 - (label.get_height()/2))
                )

            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)
        
        redraw_window(win, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((90,90,90))
        font =pygame.font.SysFont("comicsans", 60)
        label = font.render("Click to play", 1, (0,0,0))
        win.blit(label, (100, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True: 
    menu_screen()
