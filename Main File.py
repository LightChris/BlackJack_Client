import pygame
import sys
from pgu import gui
from pygame.locals import *

RESX = 800
RESY = 600
FPS = 40


class GuiWindow:
    def __init__(self):
        self.app = app = gui.App()
        button_hit = gui.Button('Hit')
        button_stand = gui.Button('Stand')
        button_double = gui.Button('Double')
        self.rect = pygame.Rect((300, 550, 175, 25))
        table = gui.Table()
        table.td(button_hit)
        table.td(button_stand)
        table.td(button_double)
        app.init(widget=table, screen=screen, area=self.rect)

    def event(self, event):
        self.app.event(event)

    def paint(self):
        fontPlayer1 = myFont.render(player1_name, 0, fontColor)
        screen.blit(fontPlayer1, (x1, y1))
        fontPlayer2 = myFont.render(player2_name, 0, fontColor)
        screen.blit(fontPlayer2, (x2, y2))
        fontPlayer3 = myFont.render(player3_name, 0, fontColor)
        screen.blit(fontPlayer3, (x3, y3))
        pygame.draw.rect(screen, (0, 100, 0), self.rect, 2)
        pygame.draw.rect(screen, (0, 120, 0), diler_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player1_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player2_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player3_rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), cards_rect, 2)
        self.app.paint()


# pygame.init()
screen = pygame.display.set_mode((RESX, RESY), 0, 32)
pygame.display.set_caption("BlackJack v0.0.1")
window = GuiWindow()
bgColor = (0, 100, 0)
screen.fill(bgColor)

fontSize = 16
fontColor = (0, 0, 0)
myFont = pygame.font.SysFont("None", fontSize, bold=False, italic=False)
x1, y1 = 100, 335
x2, y2 = 350, 335
x3, y3 = 600, 335
player1_name = "Player 1"
player2_name = "Player 2"
player3_name = "Player 3"
fontPlayer1 = myFont.render(player1_name, 0, fontColor)
# screen.blit(fontPlayer1, (x1, y1))
fontPlayer2 = myFont.render(player2_name, 0, fontColor)
# screen.blit(fontPlayer2, (x2, y2))
fontPlayer3 = myFont.render(player3_name, 0, fontColor)
# screen.blit(fontPlayer3, (x3, y3))
# fontHit = myFont.render("Hit", 0, fontColor)
# screen.blit(fontHit, (310, 558))
# fontStand = myFont.render("Stand", 0, fontColor)
# screen.blit(fontStand, (377, 558))
# fontStand = myFont.render("Double", 0, fontColor)
# screen.blit(fontStand, (450, 558))

cards_rect = Rect((600, 50), (90, 135))

diler_rect = Rect((350, 100), (90, 135))

hit_rect = Rect((281, 550), (75, 25))
stand_rect = Rect((356, 550), (75, 25))
double_rect = Rect((431, 550), (75, 25))

player1_rect = Rect((100, 350), (90, 135))
player2_rect = Rect((350, 350), (90, 135))
player3_rect = Rect((600, 350), (90, 135))

# pygame.draw.rect(screen, (255, 255, 255), cards_rect, 2)
# pygame.draw.rect(screen, (255, 255, 255), hit_rect, 2)
# pygame.draw.rect(screen, (255, 255, 255), double_rect, 2)
# pygame.draw.rect(screen, (255, 255, 255), stand_rect, 2)
# pygame.draw.rect(screen, (0, 120, 0), diler_rect, 2)
# pygame.draw.rect(screen, (200, 200, 0), player1_rect, 2)
# pygame.draw.rect(screen, (200, 200, 0), player2_rect, 2)
# pygame.draw.rect(screen, (200, 200, 0), player3_rect, 2)
pygame.display.update()
mainLoop = True
clock = pygame.time.Clock()
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            sys.exit()
        window.event(event)
    dt = clock.tick(FPS)
    screen.fill((0, 100, 0))
    window.paint()
    pygame.display.flip()

pygame.quit()
