import pygame
import random


vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite):


    def __init__(self,image_path,screen_width,screen_height,size,speed=2):
        super().__init__()
        

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))


        x = random.randint(0,screen_width - self.image.get_width())
        y = random.randint(-self.image.get_height() * 2,-self.image.get_height())


        self.screen_height = screen_height

        self.rect = self.image.get_rect(topleft=(x,y))

        self.vel = vec(0,speed)

    
    def update(self):

        self.rect.topleft += self.vel

        if self.rect.top > self.screen_height:
            self.kill()
    

