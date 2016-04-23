import os
import sys
import pygame
from pgu import gui
from pygame import *
from settings import *
from Classes.Dealer import *
from Classes.Player import *
from utilities import load_image
from Classes.Server import Server


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RESX, RESY), 0, 32)
        pygame.display.set_caption("BlackJack v0.1.0a")
        self.run = True
        self.deck_image = load_image(path=os.path.join("images", "cards"), name="back.png")
        self.deck_pos = (600, 50)

        # Кнопки gui:
        self.app = app = gui.App()
        self.rect = pygame.Rect((300, 550, 175, 25))
        connect_button = gui.Button("Connect")
        # connect_button.connect()
        table = gui.Table()
        table.td(connect_button)




        # Колода
        self.deck = Deck()

        # Диллер
        self.dealer = Dealer((250, 110), self.deck)

        # Список игроков
        # self.players = [Player((25, 400), self.deck), Player((275, 400), self.deck), Player((525, 400), self.deck)]
        self.players_position = ((25, 400), (275, 400), (525, 400))
        self.players = []
        self.add_player(1)
        self.add_player(2)
        self.add_player(3)
        self.server = Server()
        # TEMP
        for player in self.players:
            player.add_cards()
            player.add_cards()
        self.dealer.add_cards()
        self.dealer.add_cards()

    def add_player(self, id):
        player = Player((self.players_position[id-1]), self.deck)
        self.players.append(player)

    def render(self, screen):
        screen.blit(self.deck_image, self.deck_pos)

    def mainloop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    sys.exit()
                # window.event(event)
            # dt = clock.tick(FPS)
            self.screen.fill((0, 100, 0))
            self.render(self.screen)
            self.dealer.render(self.screen)
            for player in self.players:
                player.render(self.screen)
            pygame.display.flip()
