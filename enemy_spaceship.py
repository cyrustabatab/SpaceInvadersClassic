import pygame
import os
import random

vec = pygame.math.Vector2

def get_images(directory,size=60):
    images= []
    for file_ in os.listdir(directory):
        image = pygame.transform.scale(pygame.image.load(os.path.join(directory,file_)).convert_alpha(),(size,size))
        images.append(image)


    return images





class EnemySpaceShip(pygame.sprite.Sprite):
    
    
    image_directory = os.path.join('assets','enemy_ships')
    images =get_images(image_directory)

    def __init__(self,screen_width,screen_height,speed=2):
        super().__init__()

        self.image = random.choice(self.images)

        y = random.randint(-40,-30)
        x = random.randint(0,screen_width - self.image.get_width())


        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel = vec(0,speed)
        self.screen_height = screen_height

    

    def update(self):

        self.rect.center  += self.vel


        if self.rect.top >= self.screen_height:
            self.kill()

















