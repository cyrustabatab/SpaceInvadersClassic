import pygame
from enemy_object import EnemyObject,resize
import os



def get_meteor_images(size=100):

    directory = os.path.join('assets','meteor_images')
    
    images = []
    for file_ in os.listdir(directory):

        full_path = os.path.join(directory,file_)
        image = pygame.image.load(full_path).convert_alpha()
        image = pygame.transform.scale(image,(size,size))
        images.append(image)

    return images









class Meteor(EnemyObject):

    images = get_meteor_images()
    def __init__(self,screen_width,screen_height,speed=4,frame_switch=10,damage=20,size=-1,hits=4):
        self.image = self.images[0]
        super().__init__(screen_width,screen_height,speed,damage,hits)
        self.image_index = 0

        self.frame_count = 0
        self.frame_switch = frame_switch
        self.damage = damage


    def update(self):
        super().update()



        self.frame_count += 1

        if self.frame_count == self.frame_switch:
            self.frame_count = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]












