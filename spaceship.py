import pygame,os,random
from bullet import Bullet
from torpedo import Torpedo
from explosion_animation import Explosion
import time
from star import Star
from copy import copy

vec = pygame.math.Vector2

GREEN = (0,255,0)
RED = (255,0,0)
BLUE =(0,0,255,128)
WHITE = (255,0,0)
BLACK = (0,0,0)


class Spaceship(pygame.sprite.Sprite):

    image = pygame.image.load(os.path.join('assets','spaceship.png'))
    laser_sound = pygame.mixer.Sound(os.path.join('assets','laser.wav'))
    power_up_sound = pygame.mixer.Sound(os.path.join('assets','Powerup.wav'))
    laser_sound.set_volume(0.3)
    font = pygame.font.Font(os.path.join('assets','atari.ttf'),20)

    def __init__(self,screen_width,screen_height,xspeed=5,health=100,cooldown_time=0.5):
        super().__init__()
        
        
        self.original_image = self.image.copy() 
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.health = health
        self.full_health = self.health
        bottom_gap = 10
        self.original_pos = (self.screen_width//2 - self.image.get_width()//2,screen_height - bottom_gap - self.image.get_height())

        self.bullets = pygame.sprite.Group()        
        self.vel = vec(xspeed,0)
        self.original_vel = vec(0,-1)
        self.cooldown_time = cooldown_time

        self.rect = self.image.get_rect(topleft=(self.original_pos))
        self.cooldown = False
        self.transparent_surface = pygame.Surface((self.rect.width + 10,self.rect.height + 10),pygame.SRCALPHA)
        self.transparent_rect = self.transparent_surface.get_rect(center=self.rect.center)
        pygame.draw.circle(self.transparent_surface,BLUE,(self.transparent_rect.centerx - self.transparent_rect.x,self.transparent_rect.centery - self.transparent_rect.y),(self.transparent_rect.width )//2)

        self.protected = False
        self.protected_bubble = False
        self.hits_allowed = 0
        self.protection_timer = 5
        self.speedy = False
        self.speed_time = 5
        self.torpedo = pygame.sprite.GroupSingle()
        self.has_torpedo = False
        self.is_frozen = False
        self.poisoned = False
        self.can_turn = True

        self.angle = 0
        self.rotation_speed = 1.8#1.8
        self.direction = 0
        

        
        self.health_surface = pygame.Surface(self.image.get_size(),pygame.SRCALPHA)
        self.health_surface_rect = self.health_surface.get_rect(topleft=self.rect.topleft)
        pygame.draw.rect(self.health_surface,RED,(0,self.health_surface.get_height() - 10,self.health_surface.get_width(),10))
        pygame.draw.rect(self.health_surface,GREEN,(0,self.health_surface.get_height() - 10,(self.health/self.full_health) * self.rect.width,10))
        self.original_health_surface = self.health_surface.copy()


    

    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        elif self.direction == -1:
            self.angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        

        self.original_health_surface.fill((255,255,255,0))
        pygame.draw.rect(self.original_health_surface,RED,(0,self.original_health_surface.get_height() - 10,self.rect.width,10))
        pygame.draw.rect(self.original_health_surface,GREEN,(0,self.original_health_surface.get_height() - 10,(self.health/self.full_health) * self.original_health_surface.get_width(),10))
        self.health_surface = pygame.transform.rotate(self.original_health_surface,self.angle)
        self.health_surface_rect = self.health_surface.get_rect(center=self.health_surface_rect.center)
        #self.health_bar_image = pygame.transform.rotate(self.original_health_bar_image,self.angle)
        #self.health_bar_rect = self.health_bar_image.get_rect(center=self.health_bar_rect.center)
    

    def get_rotation(self):
        if self.direction == 1:
            self.original_vel.rotate_ip(self.rotation_speed)
        elif self.direction == -1:
            self.original_vel.rotate_ip(-self.rotation_speed)
    
    def poison(self,seconds=5):
        self.poison_time = seconds

        self.poisoned = True
        self.poisoned_start_time = time.time()
        self.last_poison_time = self.poisoned_start_time








    def add_five_hit_protection(self):
        self.protected = True
        self.hits_allowed = 5
        self.hits_allowed_text = self.font.render(str(self.hits_allowed),True,WHITE)

    

    def freeze(self,seconds=5):
        self.frozen_timer = seconds

        self.frozen_start = time.time()

        self.is_frozen = True



    
    def allow_turning(self,seconds=10):
        self.turning_timer = seconds
        self.can_turn = True
        self.original_vel = copy(self.vel)




    def add_torpedo(self):
        if not self.has_torpedo:
            self.has_torpedo = True
    
    def fire_torpedo(self):

        if not self.torpedo.sprite:
            torpedo = Torpedo(self.rect.centerx,self.rect.y)
            self.torpedo.sprite = torpedo
            self.has_torpedo = False


    def make_invincible(self):
        self.protected_bubble = True
        self.protected_start = time.time()

    def double_speed(self):
        if not self.speedy:
            self.vel *= 2
            self.speedy = True
        self.speed_start_time = time.time()

    
    def die(self,explosions):
        self.kill()
        size = 3
        explosions.add(Explosion(*self.rect.center,3))

    def add_ten_health(self):
        self.health = max(self.health + 10,self.full_health)

    def set_full_health(self):
        self.health = self.full_health

    def draw(self,screen):

        screen.blit(self.image,self.rect)
        if self.protected:
            screen.blit(self.transparent_surface,self.transparent_rect)
        if self.torpedo:
            self.torpedo.draw(screen)

        if self.has_torpedo:
            screen.blit(Torpedo.image,(5,self.screen_height - Torpedo.image.get_height() - 5))

        if self.hits_allowed:
            screen.blit(self.hits_allowed_text,(self.rect.x,self.rect.y))
    def restore_health_and_remove_bullets(self):
        self.health = self.full_health
        self.bullets.empty()
    

    def instant_die(self):
        self.health = 0

    def draw_health_bar_and_bullets(self,screen):

        
        self.bullets.draw(screen)
        #pygame.draw.rect(screen,RED,(self.rect.left - 5,self.rect.bottom + 5,self.image.get_width() + 10,10))
        #pygame.draw.rect(screen,GREEN,(self.rect.left - 5,self.rect.bottom + 5,self.health/self.full_health * (self.image.get_width() + 10),10))
        screen.blit(self.health_surface,self.health_surface_rect)

    

    def fire_bullet(self):
        
        self.laser_sound.play()
        self.bullet_fire_start_time = time.time()
        if not self.can_turn:
            bullet = Bullet(self.rect.centerx,self.rect.top,ydirection=self.original_vel.y,xdirection=self.original_vel.x)
        else:
            bullet = Bullet(self.rect.centerx,self.rect.centery,ydirection=self.original_vel.y,xdirection=self.original_vel.x,angle=self.angle)
        self.bullets.add(bullet)
        self.cooldown = True
        self.bullet_fire_start_time = time.time()


    
    def update(self,pressed_keys,alien_group,bullets_group,explosions,hearts,potions,crosses,items):
        

        current_time = time.time()
        if self.protected_bubble:
            if current_time - self.protected_start >= self.protection_timer:
                self.protected = False

        if self.cooldown:
            if current_time - self.bullet_fire_start_time >= self.cooldown_time:
                self.cooldown = False

        
        if self.speedy:
            if current_time - self.speed_start_time >= self.speed_time:
                self.vel /= 2
                self.speedy = False
        

        if self.is_frozen:
            if current_time - self.frozen_start >= self.frozen_timer:
                self.is_frozen = False
        
        if self.poisoned:

            if current_time - self.poisoned_start_time >= self.poison_time:
                self.poisoned = False
            elif current_time - self.last_poison_time >= 1:
                self.last_poison_time = current_time
                self.health -= 2
    
        if self.can_turn:
            self.set_rotation()
            self.get_rotation()


        if not self.is_frozen:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.topleft -= self.vel
                self.health_surface_rect.topleft -= self.vel
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.health_surface_rect.left = 0

            if pressed_keys[pygame.K_RIGHT]:
                self.rect.topright += self.vel
                self.health_surface_rect.topright += self.vel
                if self.rect.right > self.screen_width:
                    self.rect.right = self.screen_width
                    self.health_surface_rect.right = self.screen_width
            if pressed_keys[pygame.K_a]:
                self.direction = -1
            elif pressed_keys[pygame.K_d]:
                self.direction = 1
            else:
                self.direction = 0


            
            if not self.cooldown and pressed_keys[pygame.K_SPACE]:
                self.fire_bullet()
        
        self.transparent_rect.center = self.rect.center
        
        self.bullets.update()
        

        self.torpedo.update() 
        collisions_enemy_torpedo = None
        if self.torpedo.sprite:
        

            collisions_enemy_torpedo = pygame.sprite.spritecollide(self.torpedo.sprite,alien_group,True,collided=pygame.sprite.collide_mask)

            if collisions_enemy_torpedo:
                self.power_up_sound.play()
                alien_ship = collisions_enemy_torpedo[0]
                size = random.randint(1,3)
                explosion = Explosion(*alien_ship.rect.center,size)
                explosions.add(explosion)


            
        
        

        collisions_enemy = pygame.sprite.groupcollide(self.bullets,alien_group,True,True,collided=pygame.sprite.collide_mask)
        for _,alien_ships in collisions_enemy.items():
            for alien_ship in alien_ships:
                size = random.randint(1,3)
                explosion = Explosion(*alien_ship.rect.center,size)
                explosions.add(explosion)

        
        if not self.protected_bubble:
            collisions = pygame.sprite.spritecollide(self,bullets_group,dokill=True,collided=pygame.sprite.collide_mask)
            if collisions:
                

                if self.hits_allowed:
                    self.hits_allowed -= len(collisions)

                    self.hits_allowed_text = self.font.render(str(self.hits_allowed),True,WHITE)
                    if self.hits_allowed <= 0:
                        self.protected = False
                        self.health -= abs(self.hits_allowed) * 10
                else:
                    self.health -= 10 * len(collisions)
                    if self.health <= 0:
                        self.die(explosions)
                        return True
    
        item_collisions = pygame.sprite.spritecollide(self,items,dokill=True,collided=pygame.sprite.collide_mask)
        
        if item_collisions:
            self.power_up_sound.play()
            for item in item_collisions:
                item.powerup(self)
        

        if self.health <= 0:
            self.die(explosions)
            return True

        
        
        
        ''' 
        heart_collisions = pygame.sprite.spritecollide(self,hearts,dokill=True,collided=pygame.sprite.collide_mask)
        
        self.health += len(heart_collisions) * 10
        self.health = min(self.health,100)

        potion_collisions = pygame.sprite.spritecollide(self,potions,dokill=True,collided=pygame.sprite.collide_mask)

        if potion_collisions:
            self.protected = True
            self.protected_start = time.time()


        cross_collisions = pygame.sprite.spritecollide(self,crosses,dokill=True,collided=pygame.sprite.collide_mask)

        if cross_collisions:
            self.health = self.full_health

        '''

        return False






