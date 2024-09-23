import pygame

class ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.center = [self.x, self.y]
        
class pad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("pad.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        self.rect.center = [self.x, self.y]

class brick(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]