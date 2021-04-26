import pygame


class Renderable:
    def __init__(self, current_sprite, pos_x, pos_y, all_sprites, sprite_time, flip, depth=0):
        self.current_sprite = current_sprite
        self.x = pos_x
        self.y = pos_y
        self.all_sprites = all_sprites
        self.sprite_time = sprite_time
        self.flip_x = flip[0]
        self.flip_y = flip[1]
        self.time = 0
        self.layer = depth
        self.width = all_sprites[current_sprite[0]][current_sprite[1]].get_rect().width
        self.height = all_sprites[current_sprite[0]][current_sprite[1]].get_rect().height
        #self.mask = pygame.mask.from_surface(all_sprites[current_sprite[0]][current_sprite[1]])
