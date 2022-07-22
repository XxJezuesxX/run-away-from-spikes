# start from learning rectangles
from random import choice

import pygame
from sys import exit

from Player import Player
from Terrains import Terrains

pygame.init()
screen = pygame.display.set_mode((650, 480))
pygame.display.set_caption("Volcano esc")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/OpenSans-LightItalic.ttf", 50)
game_state = True

player = pygame.sprite.GroupSingle()
player.add(Player())

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/Shaded_cloud.png").convert()

spike_surface = pygame.image.load("graphics/Spikes.png").convert_alpha()
spike_rect = spike_surface.get_rect(center=(-28, 250))

hero_surface = pygame.image.load("graphics/hero1.png").convert_alpha()
hero_rect = hero_surface.get_rect(center=(80, 320))
hero_gravity = 0

# elements for menu screen
# hero_surface_menu = pygame.image.load("graphics/Hero_run_1.png").convert_alpha()
# hero_surface_menu = pygame.transform.rotozoom(hero_surface_menu, 0, 2)
# hero_surface_menu_rect = hero_surface_menu.get_rect(center=(300, 150))

obstacle_group = pygame.sprite.Group()

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

x = 0

while True:

    # this loop stack ques a user's command and execute according to the code written in the loop
    for event in pygame.event.get():
        # this command is used to listen to 'x' button to close the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == obstacle_timer:
            obstacle_group.add(Terrains(choice([1, 2, 3])))
            obstacle_group.add(Terrains(choice([1, 2, 3, 3])))
            obstacle_group.add(Terrains(choice([2, 2, 3])))

    if game_state:

        # rel_x contains the value of the rightmost x coordinate of the background
        rel_x = x % sky_surface.get_rect().width
        x -= 1

        # part of the image that is going towards left
        show_image = rel_x - sky_surface.get_rect().width
        screen.blit(sky_surface, (show_image, 0))

        if rel_x < 650:
            screen.blit(sky_surface, (rel_x, 0))

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        screen.blit(ground_surface, (0, 470))
        screen.blit(spike_surface, spike_rect)

    pygame.display.update()
    clock.tick(60)
