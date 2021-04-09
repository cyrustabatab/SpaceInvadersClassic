import pygame
import random
from enemy_spaceship import get_images
from meteor import Meteor
import os


def get_black_hole_images(size=60):

    directory = os.path.join('assets','black_hole')
    images = []
    for file_ in os.listdir(directory):
        image = pygame.transform.scale(pygame.image.load(os.path.join(directory,file_)).convert_alpha(),(size,size))
        images.append(image)
    return images


class BlackHole(Meteor):
    

    images = [get_images(os.path.join('assets','black_hole',directory)) for directory in os.listdir(os.path.join('assets','black_hole'))]
    def __init__(self,screen_width,screen_height,speed=4,frame_switch=5,damage=float("inf"),hits=float("inf")):
        self.images = random.choice(self.images)
        super().__init__(screen_width,screen_height,speed,frame_switch,damage,hits)






