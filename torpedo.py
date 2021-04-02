import pygame
from item import Item
import os
import textwrap

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

    name = 'torpedo'    

    @property
    def image_path(self):
        return os.path.join('assets','torpedoTed.png')
    

    @property
    def text(self):
        text = "POWERFUL PERSISTENT WEAPON THAT IS NOT DESTROYED ON IMPACT WITH ENEMIES. HIT ENTER TO USE AND CAN ONLY HOLD ONE TORPEDO AT A TIME."
        phrases = textwrap.wrap(text,30)
        WHITE = (255,255,255)
        texts = []
        for phrase in phrases:
            text = self.font.render(phrase,True,WHITE)
            texts.append(text)
        return texts
    

    def powerup(self,player):
        player.add_torpedo()














