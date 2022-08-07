from random import randint

import pygame


class Terrains(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 1:
            terrain1 = pygame.image.load("graphics/ground1.png").convert_alpha()
            self.image = terrain1

        elif type == 2:
            terrain2 = pygame.image.load("graphics/ground2.png").convert_alpha()
            self.image = terrain2

        elif type == 3:
            terrain3 = pygame.image.load("graphics/ground3.png").convert_alpha()
            self.image = terrain3

        self.animation_index = 0
        self.rect = self.image.get_rect(midbottom=(630, randint(100, 480)))

        # self.direction = pygame.math.Vector2()
        # self.direction.y = -2

    def destroy_useless_terrains(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):

        # rate of change of platform's y direction
        self.rect.x -= 2
        self.destroy_useless_terrains()

