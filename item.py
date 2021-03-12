import pygame


vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite):


    def __init__(self,screen_width,image,speed=2):
        super().__init__()
        

        x = random.randint(0,screen_width - image.get_width())
        y = random.randint(-image.get_height() * 2,-image.get_height())


        self.image = image


        self.rect = self.image.get_rect(topleft=(x,y))

        self.vel = vec(0,speed)

    
    def update(self):

        self.rect.topleft += self.vel
    

