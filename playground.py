from random import choice, randint

import pygame
from sys import exit

from Player import Player
from Terrains import Terrains

# formalities
pygame.init()
screen = pygame.display.set_mode((650, 480))
pygame.display.set_caption("Volcano esc")
clock = pygame.time.Clock()

# controls whether game is running or not
game_state = True

player_draw = pygame.sprite.GroupSingle()
player = Player()
player_draw.add(player)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/Shaded_cloud.png").convert()

spike_surface = pygame.image.load("graphics/Spikes.png").convert_alpha()
spike_rect = spike_surface.get_rect(center=(-28, 250))

platform_group = pygame.sprite.Group()

# Timer
timer = pygame.USEREVENT + randint(0, 1)
pygame.time.set_timer(timer, randint(1500, 1700))

x = 0

while True:

    # this loop ques a user's command and execute according to the code written in the loop
    for event in pygame.event.get():
        # this command is used to listen to 'x' button to close the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == timer:
            i = randint(0,4)
            if i == 0:
                platform_group.add(Terrains(choice([1, 2, 3])))
                platform_group.add(Terrains(choice([2, 3, 3])))
            elif i == 1:
                platform_group.add(Terrains(choice([1, 2, 3, 3])))
                platform_group.add(Terrains(choice([1, 2, 3])))
            elif i == 2:
                platform_group.add(Terrains(choice([2, 3, 3])))
            elif i == 3:
                platform_group.add(Terrains(choice([1, 1, 2])))
                platform_group.add(Terrains(choice([1, 3, 2])))

    if game_state:

        # rel_x contains the value of the rightmost x coordinate of the background
        rel_x = x % sky_surface.get_rect().width
        x -= 1

        # animating the background of the game
        show_image = rel_x - sky_surface.get_rect().width
        screen.blit(sky_surface, (show_image, 0))

        if rel_x < 650:
            screen.blit(sky_surface, (rel_x, 0))  #

        # calling terrain
        platform_group.draw(screen)
        platform_group.update()  #

        # calling the player
        player_draw.draw(screen)
        player.update()  #

        # horizontal_collision(player, terrain_group)
        # vertical_collision(player, terrain_group)

        screen.blit(ground_surface, (0, 470))
        screen.blit(spike_surface, spike_rect)

    pygame.display.update()
    clock.tick(60)
