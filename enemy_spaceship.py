import pygame
import os
import random
import time
from spritesheet import Spritesheet

vec = pygame.math.Vector2

RED = (255,0,0)
GREEN = (0,255,0)

def get_images(directory,size=60):
    images= []
    for file_ in os.listdir(directory):
        path = os.path.join(directory,file_)
        if os.path.isfile(path):
            image = pygame.image.load(path).convert_alpha()
            if size != -1:
                image = pygame.transform.scale(image,(size,size))

            images.append(image)


    return images



class EnemySpaceShips:

    def __init__(self):
        self.ships = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def add_ship(self,ship):    
        self.ships.add(ship)

    
    def reset(self):

        self.ships.empty()
        self.bullets.empty()

    def add_bullet(self,bullet):
        self.bullets.add(bullet)
    

    def draw(self,screen):

        
        for ship in self.ships:
            ship.draw(screen)
        #self.bullets.draw(screen)
    
    def update(self):

        self.ships.update()
        self.bullets.update()





class EnemySpaceShip(pygame.sprite.Sprite):
    
    
    image_directory = os.path.join('assets','enemy_ships')
    images =get_images(image_directory)

    class EnemyBullet(pygame.sprite.Sprite):


        image = pygame.image.load(os.path.join('assets','enemy_ship_bullet.png')).convert_alpha()


        def __init__(self,x,y,screen_height,speed,size=20,damage=10):
            super().__init__()
            
            #self.image = pygame.transform.scale(self.image,(size,size))
            self.image = pygame.transform.scale(self.image,(size,size))
            self.screen_height = screen_height
            self.rect = self.image.get_rect(center=(x,y))
            self.mask = pygame.mask.from_surface(self.image)
            self.vel  = vec(0,speed)#vec(0,speed)
            self.damage = damage
    

        def update(self):

            self.rect.center += self.vel
            if self.rect.top >= self.screen_height:
                self.kill()

    def __init__(self,screen_width,screen_height,speed=2,health=100):
        super().__init__()
        
        self.image = random.choice(self.images)

        y = random.randint(-40,-30)
        x = random.randint(0,screen_width - self.image.get_width())


        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel = vec(0,speed)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.full_health = health
        self.health = health
        self.start_time = time.time()
        self.next_fire_time = random.randint(1,3) #fire beetween 1 and 3 seconds
        self.bullets = pygame.sprite.Group()
    
    
    def take_damage(self,damage):


        self.health -= damage

        if self.health <= 0:
            self.kill()
            return True

        return False

    
    def fire_bullet(self):
        bullet = EnemySpaceShip.EnemyBullet(*self.rect.center,self.screen_height,self.vel.y * 2)
        self.bullets.add(bullet)


    def draw(self,screen):

        offset = 5

        pygame.draw.rect(screen,RED,(self.rect.left - offset,self.rect.bottom + offset,self.rect.width + offset,offset))
        pygame.draw.rect(screen,GREEN,(self.rect.left - offset,self.rect.bottom + offset,(self.health/self.full_health) * (self.rect.width + offset),offset))
        self.bullets.draw(screen)
        screen.blit(self.image,self.rect)


    

    def update(self):
        

        current_time = time.time()

        if current_time -  self.start_time >= self.next_fire_time:
            self.fire_bullet()
            self.start_time = current_time
        self.rect.center  += self.vel
        
        self.bullets.update()

        if self.rect.top >= self.screen_height:
            self.kill()
            #self.kill()



def get_rocket_images():

    directory = os.path.join('assets','rocket_ship')
    images = []
    for file_ in os.listdir(directory):
        image = pygame.image.load(os.path.join(directory,file_)).convert_alpha()
        image = pygame.transform.rotate(image,-90)
        images.append(image)


    return images






class RocketShip(EnemySpaceShip):

    
    images = get_rocket_images()
    switch_frame = 10

    def __init__(self,screen_width,screen_height,speed=5,health=100):
        super().__init__(screen_width,screen_height,speed,health)
        self.frame_count = 0
        self.image_index = 0
        self.image = self.images[self.image_index]




    def update(self):
        super().update()

        self.frame_count += 1

        if self.frame_count == self.switch_frame:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.frame_count = 0

def get_flying_saucer_images():
    
    '''load from spritesheet the different hues'''
    example_images = get_images(os.path.join('assets','flying_saucer'),size=-1)

    spritesheets_directory = os.path.join("assets",'flying_saucer','spritesheets')
    
    num_rows = 6
    different_images = [example_images]
    width,height = 40,30
    for spritesheet in os.listdir(spritesheets_directory):
        path = os.path.join(spritesheets_directory,spritesheet)
        sheet = Spritesheet(path)
        images = [] 
        for row in range(num_rows):
            image = sheet.load_strip((0,row * height,width,height),1)[0] # returns a list but we know its 1 image
            images.append(image)
        different_images.append(images)
    return different_images







class BlackHole(RocketShip):

    images = get_images(os.path.join('assets','black_hole'))


    def __init__(self,screen_width,screen_height,speed=3,health=0):
        super().__init__(screen_width,screen_height,speed,health)















class FlyingSaucer(RocketShip):

    '''behavior of flying saucer is very similar to rocket ship except update method will be slightly differen in future'''


    hue_images = get_flying_saucer_images()

    def __init__(self,screen_width,screen_height,speed=3,health=100):
        self.images = random.choice(self.hue_images)
        super().__init__(screen_width,screen_height,speed,health)

        self.x_speed = random.choice((-1,1)) * random.randint(3,5)
        self.y_speed = random.randint(3,5)

        self.vel = vec(self.x_speed,self.y_speed)
        self.second_time = time.time()

    def fire_bullet(self):
        bullet = EnemySpaceShip.EnemyBullet(*self.rect.center,self.screen_height,abs(self.vel.y) * 2)
        self.bullets.add(bullet)
    
    def update(self):
        super().update()
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.vel.x *= -1
        
        if (self.rect.top < 0 and self.vel.y < 0) or (self.rect.bottom > self.screen_height):
            self.vel.y *= -1

        current_time = time.time()
        

        new_speed = lambda value: random.randint(3,5) * (-1 if value < 0 else 1)
        if current_time - self.second_time  >= 1:
            if random.randint(1,2) == 1:
                self.vel.x *= -1
                self.vel.x = new_speed(self.vel.x)
                

            if random.randint(1,2) == 1: 
                self.vel.y *= -1
                self.vel.y = new_speed(self.vel.y)

            self.second_time = current_time







