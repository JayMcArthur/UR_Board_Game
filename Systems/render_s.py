import pygame
import Assets.esper as esper
from Components.renderable_c import Renderable


class RenderSystem(esper.Processor):
    def __init__(self, window, clear_color):
        super().__init__()
        self.window = window
        self.clear_color = clear_color

    def process(self):
        # Get window in case it changed > Alt + Enter
        self.window = pygame.display.get_surface()

        # Clear the window:
        self.window.fill(self.clear_color)

        # This will iterate over every Entity that has this Component
        for ent, rend in self.world.get_component(Renderable):
            # Blit the Entity
            self.window.blit(pygame.transform.flip(rend.all_sprites[rend.current_sprite[0]][rend.current_sprite[1]], rend.flip_x, rend.flip_y), (rend.x, rend.y))

            # Check if there is a sprite timer
            if rend.sprite_time[rend.current_sprite[0]][rend.current_sprite[1]] != -1:
                # Update amount of time we have been on the current sprite
                rend.time = (rend.time + 1) % rend.sprite_time[rend.current_sprite[0]][rend.current_sprite[1]]
                # If time is up move on to the next sprite
                if rend.time == 0:
                    rend.current_sprite[1] = (rend.current_sprite[1] + 1) % len(rend.all_sprites[rend.current_sprite[0]])
                    rend.width = rend.all_sprites[rend.current_sprite[0]][rend.current_sprite[1]].get_rect().width
                    rend.height = rend.all_sprites[rend.current_sprite[0]][rend.current_sprite[1]].get_rect().height

            # Update the mask encase of flip or sprite change
            # rend.mask = pygame.mask.from_surface(pygame.transform.flip(rend.all_sprites[rend.current_sprite[0]][rend.current_sprite[1]], rend.facing_left, 0))

        # Flip the frame
        pygame.display.flip()