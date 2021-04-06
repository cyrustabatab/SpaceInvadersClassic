import pygame
import os
from enemy_object import EnemyObject
from spritesheet import Spritesheet
from meteor import Meteor


def load_asteroid_images(size=40):
    file_path = os.path.join('assets','asteroidspritesheet.png') 

    sheet = Spritesheet(file_path)

    images = []
    width = height = 72
    for row in range(4):
        if row < 3:
            num_images = 5
        else:
            num_images = 4

        images.extend(sheet.load_strip((0,row * height,width,height,size),num_images))
    

    return images










class Asteroid(Meteor):

    images = load_asteroid_images()

    def __init__(self,screen_width,screen_height,speed=2,frame_switch=5,damage=20,size=40,hits=4):
        super().__init__(screen_width,screen_height,speed,frame_switch,damage,size,hits)




