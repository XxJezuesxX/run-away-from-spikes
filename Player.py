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
        self.images_run_list = [hero_rs2, hero_rs3, hero_rs4, hero_rs5, hero_rs6, hero_rs7, hero_rs8, hero_rs9]

        self.image = self.images_run_list[self.hero_index]

        self.player_jump = pygame.image.load('graphics/Lava.png').convert_alpha()
        self.rect = self.image.get_rect(center=(55, 470))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.gravity -= 7
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= 5

    def correct_position(self):
        if self.rect.x > 615:
            self.rect.x = 15
        if self.rect.x < 15:
            self.rect.x = 15

    def apply_gravity(self):
        self.gravity += 0.9
        self.rect.y += self.gravity

        if self.rect.bottom > 470:
            self.rect.bottom = 470

        if self.rect.top < 0:
            self.rect.top = 0

    def animate_char(self):

        keys = pygame.key.get_pressed()

        if self.rect.bottom != 470:
            self.image = self.player_jump

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.hero_index += 0.15
            if self.hero_index >= len(self.images_run_list):
                self.hero_index = 0
            self.image = self.images_run_list[int(self.hero_index)]

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.hero_index += 0.15
            if self.hero_index >= len(self.images_run_list):
                self.hero_index = 0
            self.image = self.images_run_list[int(self.hero_index)]
            self.image = pygame.transform.flip(self.image, True, False)

        # else:
        #
        #     if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #         self.image = self.image_rest
        #         # self.image = pygame.transform.flip(self.image, True, False)
        #     else:
        #         self.image = self.image_rest
        #         self.image = pygame.transform.flip(self.image, True, False)

    def update(self):

        self.apply_gravity()
        self.player_input()
        self.animate_char()
        self.correct_position()
