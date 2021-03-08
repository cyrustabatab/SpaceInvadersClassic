import pygame,os

vec = pygame.math.Vector2


class Heart(pygame.sprite.Sprite):

    image = pygame.transform.scale(pygame.image.load(os.path.join('assets','heart.png')).convert_alpha(),(20,20))


    def __init__(self,x,y,speed=2):
        super().__init__()

    
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)

        self.vel = vec(0,speed)
    

    def update(self):

        self.rect.center += self.vel

        if self.rect.top >= 800:
            self.kill()

