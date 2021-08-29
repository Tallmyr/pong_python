import pygame
import random


class Actor(pygame.sprite.Sprite):
    def __init__(self, width, height, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (20, height / 2) if player else (width - 20, height / 2)

        self.score = 0

        self.vy = 0

    def update(self):
        self.vy = min(self.vy, 3)
        self.vy = max(self.vy, -3)
        self.rect.y += self.vy


class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.center = (width / 2, height / 2)
        self.rect.center = self.center

        #  Set Ball Moving
        self.vx = -2
        self.vy = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def reset(self, score):
        self.rect.center = self.center
        if dir == "opponent":
            self.vx = -2
        elif dir == "player":
            self.vx = 2
        self.vy = random.randint(-3, 3)
