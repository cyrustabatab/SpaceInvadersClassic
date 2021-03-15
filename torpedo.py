import pygame
from item import Item
import os

vec = pygame.math.Vector2

class Torpedo(pygame.sprite.Sprite):
    image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets','torpedoTed.png')).convert_alpha(),(40,40)),-90)
    sound = pygame.mixer.Sound(os.path.join('assets','missile.wav'))
    def __init__(self,x,y,speed=4):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midbottom=(x,y))
        self.vel = vec(0,-speed)
        self.sound.play(-1)
    



    def update(self):
        self.rect.center += self.vel
        
        if self.rect.bottom < 0:
            self.sound.stop()
            self.kill()




class TorpedoPowerUp(Item):

    image_path = os.path.join('assets','torpedoTed.png')

    def __init__(self,screen_width,screen_height,size=40):
        super().__init__(self.image_path,screen_width,screen_height,size,rotate=90)


    def powerup(self,player):
        player.add_torpedo()














