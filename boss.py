import pygame,os
import time
import random

vec = pygame.math.Vector2

def get_hatch_sequence(directory,size=-1):
    directory = os.path.join('assets','boss_images',directory)
    images = []
    for file_ in os.listdir(directory):
        image = pygame.image.load(os.path.join(directory,file_)).convert_alpha()
        if size != -1:
            image = pygame.transform.scale(image,(size,size))

        images.append(image)

    return images




class Boss(pygame.sprite.Sprite):

    hatch_sequence = get_hatch_sequence('hatch_sequence',size=40)
    boss_sequence= get_hatch_sequence('boss_sequence')
    ring = pygame.image.load(os.path.join('assets','boss_images','ring.png'))
    def __init__(self,screen_width,screen_height):
        super().__init__()
        self.images = self.hatch_sequence
        self.image  = self.images[0]
        self.rect = self.image.get_rect(center=(screen_width//2,self.ring.get_height()//2))
        self.screen_width = screen_width        
        self.screen_height = screen_height
        self.ring_rect = self.ring.get_rect(center=(screen_width//2,self.ring.get_height()//2))
        self.frame_count = 0
        self.image_index = 0
        self.hatched = False
        self.vel=  vec(1,1)


    
    def draw(self,screen):

        screen.blit(self.image,self.rect)
        if self.hatched:
            screen.blit(self.ring,self.ring_rect)



    def update(self):
        self.frame_count += 1
        if not self.hatched:

            if self.frame_count == 60:
                self.image_index = (self.image_index + 1) % len(self.hatch_sequence)
                self.image = self.images[self.image_index]
                self.frame_count = 0
                if self.image_index == 0:
                    self.hatched = True
                    self.images= self.boss_sequence
                    self.image = self.images[0]
                    self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
                    self.start_time = time.time()

                
        else:
            self.rect.center += self.vel
            self.ring_rect.center += self.vel
            current_time = time.time()

            if current_time - self.start_time >= 2:
                number = random.randint(1,3)
                if number == 2:
                    self.vel.x *= -1
                elif number == 3:
                    self.vel.y *= -1

                self.start_time = time.time()
                


            if self.rect.left <= 0:
                self.vel.x *= -1
            elif self.rect.right >=self.screen_width:
                self.vel.x *= -1
            elif self.rect.bottom >= 700:
                self.vel.y *= -1
            elif self.rect.top <= 0:
                self.vel.y *= -1



            if self.frame_count == 10:
                self.image_index = (self.image_index + 1) % len(self.hatch_sequence)
                self.image = self.images[self.image_index]
                self.frame_count = 0







