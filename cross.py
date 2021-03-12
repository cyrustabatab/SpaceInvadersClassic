import pygame,os,random


vec = pygame.math.Vector2


class Cross(pygame.sprite.Sprite):


    image = pygame.transform.scale(pygame.image.load(os.path.join('assets','cross.png')),(40,40))

    def __init__(self,screen_width,speed=2):
        super().__init__()


        x = random.randint(0,screen_width - self.image.get_width())

        y = random.randint(-self.image.get_height() * 2,-self.image.get_height())


        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)

        self.vel = vec(0,speed)
    


    def update(self):


        self.rect.topleft += self.vel






