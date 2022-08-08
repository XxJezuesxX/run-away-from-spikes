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
        self.gravity = 0
        self.image_rest = hero_rs1
        self.images_run_list = [hero_rs2, hero_rs3, hero_rs4, hero_rs5, hero_rs6, hero_rs7, hero_rs8,
                                hero_rs9]  # animates my player
        self.image = self.images_run_list[self.hero_index]
        self.rect = self.image.get_rect(center=(200, 200))

        self.player_jump = pygame.image.load('graphics/hero1.png').convert_alpha()

        self.is_resting_forward = True
        self.is_jumping = False

    def animate_char(self):

        keys = pygame.key.get_pressed()

        # animate character when on platform
        if self.rect.bottom != 470:
            self.image = self.player_jump
            self.is_jumping = True

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

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:

            # have to add another condition in the if statement - when the player is standing on the ground
            if self.rect.bottom == 470:
                self.gravity -= 20
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 5
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x += -5
        else:
            self.rect.x += 0

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
        self.gravity += 0.9
        self.rect.y += self.gravity

        # doesn't fall off the screen
        if self.rect.bottom > 470:
            self.rect.bottom = 470

        # maximum height it can reach
        if self.rect.top < 0:
            self.rect.top = 0

    '''
        problem - 
            3) unable to land player satisfyingly on the terrain
            4) player slipping towards left (idk at what condition(s))
    '''

    # when player is on a platform
    def vertical_collision(self):
        import playground

        keys = pygame.key.get_pressed()

        for platform in playground.platform_group:

            if self.rect.colliderect(platform.rect) and self.rect.bottom > platform.rect.centerx and self.is_jumping == True:

                # y-cor - lets me stay on platform's height (y cor)
                self.rect.bottom = platform.rect.top

                # x-axis - player's x cor change is aligned to platform's x cor's change
                self.rect.x -= 2 # terrain and player have the same speed in this case

    def update(self):

        self.physics()
        self.player_input()
        self.vertical_collision()
        self.animate_char()
        self.correct_position()
