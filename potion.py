import pygame,os,random

vec = pygame.math.Vector2

file_name = 'potion.png'

class InvincibilityPotion(pygame.sprite.Sprite):

    image = pygame.transform.scale(pygame.image.load(os.path.join('assets',file_name)),(40,40))


    def __init__(self,screen_width,speed=2):
        super().__init__()
        

        y = random.randint(-30,-20)
        x = random.randint(0,screen_width - self.image.get_width())

        self.vel = vec(0,speed)

        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)


    
    def update(self):

        self.rect.topleft += self.vel










