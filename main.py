# Import Asset Scripts
import Assets.esper as esper
import pygame

# Game Systems
import Systems.turn_s as TurnSystem
import Systems.render_s as RenderSystem

# Game Entities
import Entities.chip_e as ChipEntity
import Entities.board_e as Board

# Settings
import Assets.settings as cfg

class Main:
    def __init__(self):
        # Setup Pygame
        pygame.init()
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.QUIT)
        pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
        self.window = pygame.display.set_mode(cfg.RESOLUTION)
        self.clock = pygame.time.Clock()

        # Make Game vars
        self.playersTurn = 0
        self.win = -1

        # Initialize Esper World
        self.world = esper.World()

        # Create Entities

    def core_game_loop(self):
        self.world.process()




if __name__ == '__main__':
    game = Main()
    game.core_game_loop()
