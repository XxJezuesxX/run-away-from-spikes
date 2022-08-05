import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # hero_runstate-n
        hero_rs1 = pygame.image.load("graphics/hero1.png").convert_alpha()
        hero_rs2 = pygame.image.load("graphics/hero2.png").convert_alpha()
        hero_rs3 = pygame.image.load("graphics/hero3.png").convert_alpha()
        hero_rs4 = pygame.image.load("graphics/hero4.png").convert_alpha()
        hero_rs5 = pygame.image.load("graphics/hero5.png").convert_alpha()
        hero_rs6 = pygame.image.load("graphics/hero6.png").convert_alpha()
        hero_rs7 = pygame.image.load("graphics/hero7.png").convert_alpha()
        hero_rs8 = pygame.image.load("graphics/hero8.png").convert_alpha()
        hero_rs9 = pygame.image.load("graphics/hero9.png").convert_alpha()

        self.hero_index = 0
        self.image_rest = hero_rs1
        self.images_run_list = [hero_rs2, hero_rs3, hero_rs4, hero_rs5, hero_rs6, hero_rs7, hero_rs8,
                                hero_rs9]  # animates my player
        self.image = self.images_run_list[self.hero_index]
        self.rect = self.image.get_rect(center=(200, 200))

        self.player_jump = pygame.image.load('graphics/hero1.png').convert_alpha()

        self.is_resting_forward = True
        self.direction = pygame.math.Vector2()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -10
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 5
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -5
        else:
            self.direction.x = 0

    def correct_position(self):
        if self.rect.x > 615:
            self.rect.x = 15
        if self.rect.x < 15:
            self.rect.x = 15

    '''
    real world physics applied on character - 
        1) gravity,
        2) not falling on the ground, 
        3) not going out of the screen
        4) not fall from terrain while standing on it
    '''

    def physics(self):
        # gravity
        self.direction.y += 0.9
        self.rect.y += self.direction.y

        # doesn't fall off the screen
        if self.rect.bottom > 470:
            self.rect.bottom = 470

        # maximum height it can reach
        if self.rect.top < 0:
            self.rect.top = 0

    # making physics of the game

    '''
    problems - 
        2) cant run on the terrain as it stays at a fixed position on it
    '''

    def vertical_collision(self):
        import playground
        can_jump = True
        keys = pygame.key.get_pressed()
        for terrain in playground.terrain_group:

            if self.rect.colliderect(terrain.rect) and can_jump and self.image == self.player_jump:

                if self.rect.bottom >= terrain.rect.top:
                    self.rect.bottom = terrain.rect.top
                    if keys[pygame.K_w] or keys[pygame.K_UP]:
                        can_jump = False
                    else:
                        can_jump = True

        # elif self.rect.y < 0:
        #     self.rect.top = terrain.rect.bottom

    def animate_char(self):

        keys = pygame.key.get_pressed()

        if self.rect.bottom != 470:
            self.image = self.player_jump

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:

            self.hero_index += 0.15

            if self.hero_index >= len(self.images_run_list):
                self.hero_index = 0

            self.image = self.images_run_list[int(self.hero_index)]
            self.is_resting_forward = True

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:

            self.hero_index += 0.15

            if self.hero_index >= len(self.images_run_list):
                self.hero_index = 0

            self.image = self.images_run_list[int(self.hero_index)]
            self.image = pygame.transform.flip(self.image, True, False)
            self.is_resting_forward = False

        else:

            if self.is_resting_forward:
                self.image = self.image_rest
            else:
                self.image = self.image_rest
                self.image = pygame.transform.flip(self.image, True, False)

    def update(self):

        self.physics()
        self.player_input()
        self.rect.x += self.direction.x
        self.vertical_collision()
        self.animate_char()
        self.correct_position()
