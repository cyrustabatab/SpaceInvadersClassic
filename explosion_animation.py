import pygame,os,random


def get_explosion_images(size):

    file_names = [os.path.join('assets',f"exp{i}.png") for i in range(1,6)]
    
    images = []

    for file_name in file_names:
        image = pygame.image.load(file_name).convert_alpha()
        if size == 1:
            image = pygame.transform.scale(image,(20,20))
        elif size == 2:
            image = pygame.transform.scale(image,(40,40))
        elif size == 3:
            image = pygame.transform.scale(image,(160,160))
        images.append(image)

    return images



class Explosion(pygame.sprite.Sprite):

    mapping= {1: get_explosion_images(1),2: get_explosion_images(2),3: get_explosion_images(3)}

    explosion_sounds = [pygame.mixer.Sound(os.path.join('assets','explosion.wav')),pygame.mixer.Sound(os.path.join('assets','explosion2.wav'))]
    def __init__(self,x,y,size,explosion_speed=3):
        super().__init__()
        
        explosion_sound = random.choice(self.explosion_sounds)
        explosion_sound.play()
        self.index = 0
        self.images = self.mapping[size]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x,y))
        self.explosion_speed = explosion_speed #number of frames per image
        self.frame_counter = 0

    
    def update(self):


        self.frame_counter += 1

        if self.frame_counter == self.explosion_speed:
            self.frame_counter =0
            if self.index == len(self.images) - 1:
                self.kill()
                return
            self.index = (self.index + 1) % len(self.images)

            self.image = self.images[self.index]



















