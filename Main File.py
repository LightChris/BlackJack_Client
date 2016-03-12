import pygame
import sys
import os
from pgu import gui
from pygame.locals import *
from Deck import *

RESX = 800
RESY = 600
FPS = 40
CLICKED = 0


class GuiWindow:
    def __init__(self):
        self.app = app = gui.App()
        button_hit = gui.Button('Hit')
        button_hit.connect(gui.CLICK, self.hit_click, '')
        button_stand = gui.Button('Stand')
        # button_double = gui.Button('Double')
        self.rect = pygame.Rect((300, 550, 175, 25))
        table = gui.Table()
        table.td(button_hit)
        table.td(button_stand)
        # table.td(button_double)
        app.init(widget=table, screen=screen, area=self.rect)

    def hit_click(self, but_event):
        # CLICKED += 1
        ranks = "23456789tjqka"
        suits = "dchs"
        cards = [(s, r) for r in ranks for s in suits]
        random.shuffle(cards)
        card_name = str(cards[-1][0] + cards[-1][1] + ".png")
        print(card_name)
        self.card_name = load_image("images/cards", card_name, 1)

    def event(self, event):
        self.app.event(event)

    def paint(self):
        screen.blit(fontPlayer1, (x1, y1))
        screen.blit(fontPlayer2, (x2, y2))
        screen.blit(fontPlayer3, (x3, y3))
        pygame.draw.rect(screen, (0, 100, 0), self.rect, 2)
        pygame.draw.rect(screen, (0, 120, 0), diler_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player1_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player2_rect, 2)
        pygame.draw.rect(screen, (200, 200, 0), player3_rect, 2)
        if CLICKED == 1:
            screen.blit(self.card_name, (80, 350))
        screen.blit(card_back, (600, 50))
        screen.blit(card_ca, (340, 110))
        screen.blit(card_back, (360, 110))
        self.app.paint()


def load_image(path, name, alpha_channel):
    fullname = os.path.join(path, name)  # Указываем путь к папке с картинками
    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_channel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


screen = pygame.display.set_mode((RESX, RESY), 0, 32)
pygame.display.set_caption("BlackJack v0.1.0a")
window = GuiWindow()
bgColor = (0, 100, 0)
screen.fill(bgColor)

card_back = load_image("images/cards", "back.png", 1)
card_ca = load_image("images/cards", "ca.png", 1)

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
fontPlayer2 = myFont.render(player2_name, 0, fontColor)
fontPlayer3 = myFont.render(player3_name, 0, fontColor)

diler_rect = Rect((350, 100), (90, 135))

hit_rect = Rect((281, 550), (75, 25))
stand_rect = Rect((356, 550), (75, 25))
double_rect = Rect((431, 550), (75, 25))

player1_rect = Rect((100, 350), (90, 135))
player2_rect = Rect((350, 350), (90, 135))
player3_rect = Rect((600, 350), (90, 135))

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
