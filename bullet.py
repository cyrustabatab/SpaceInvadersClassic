import pygame,os

vec = pygame.math.Vector2

class Bullet(pygame.sprite.Sprite):

    image_1 = pygame.image.load(os.path.join('assets','bullet.png')).convert_alpha()
    image_2 = pygame.image.load(os.path.join('assets','alien_bullet.png')).convert_alpha()

    def __init__(self,x,y,direction=-1,speed=5):
        super().__init__()
        
        self.image = self.image_1 if direction == -1 else self.image_2
        
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0,direction * speed)
        self.mask = pygame.mask.from_surface(self.image)



    def update(self):


        self.rect.topleft += self.vel

        if self.rect.bottom < 0 or self.rect.top > 800:
            self.kill()


        
        





