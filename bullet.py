import pygame,os

vec = pygame.math.Vector2

class Bullet(pygame.sprite.Sprite):

    original_image_1 = pygame.image.load(os.path.join('assets','bullet.png')).convert_alpha()
    original_image_2 = pygame.image.load(os.path.join('assets','alien_bullet.png')).convert_alpha()

    def __init__(self,x,y,alien=False,ydirection=-1,xdirection=0,speed=5,angle=0):
        super().__init__()
        
        self.image = self.original_image_1 if not alien else self.original_image_2
        
        if angle != 0:
            self.image = pygame.transform.rotate(self.original_image_1,angle)
        
        self.alien = alien
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(xdirection,ydirection) * speed
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y



    def update(self):
        

        
        #self.rect.topleft += self.vel
        self.x += self.vel.x
        self.y += self.vel.y
        self.rect.center = (self.x,self.y)

        if not self.alien:
            print("vel",self.vel)
            print("pos",self.rect.topleft)
        if self.rect.bottom < 0 or self.rect.top > 800:
            self.kill()


        
        





