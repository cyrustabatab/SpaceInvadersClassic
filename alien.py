import pygame,os,random,time
from bullet import Bullet


def load_images():
    alien_image_paths = [os.path.join('assets',f"alien{i}.png") for i in range(1,6)]
    alien_images =[]
    for alien_image_path in alien_image_paths:
        alien_image = pygame.image.load(alien_image_path).convert_alpha()
        alien_images.append(alien_image)

    return alien_images



class Alien(pygame.sprite.Sprite):

    alien_images = load_images()

    def __init__(self,x,y):
        super().__init__()

        self.image = random.choice(self.alien_images)

        self.rect = self.image.get_rect(center=(x,y))
        self.frame_counter = 0
        self.direction = 1
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
    


    
    def fire_bullet(self,bullet_speed):

        bullet = Bullet(self.rect.centerx,self.rect.bottom,bullet_speed)
        return bullet

    
    def update(self):
        


        self.frame_counter += 1
        if self.frame_counter == 125:
            self.direction *= -1
            self.frame_counter = 0
        self.rect.x += self.direction * self.speed

    

    def draw(self,screen):
        screen.blit(self.image,self.rect)

