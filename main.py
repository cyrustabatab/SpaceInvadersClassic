import pygame,sys,os,time,random,math
pygame.init()

WIDTH,HEIGHT = 600,800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))

import textwrap
from spaceship import Spaceship
from aliens import Aliens
from boss import Boss
from heart import Heart
from potion import InvincibilityPotion
from cross import Cross
from star import Star
from skull import Skull
from torpedo import TorpedoPowerUp
from button import Button
from text import Text
from safety import Safety
from bomb import BombPowerUp
from snowflake import Snowflake
from poison_muk import PoisonMuk
from free_movement import FreeMovement
from fireball import Fireball
from meteor import Meteor
from asteroid import Asteroid
from enemy_spaceship import EnemySpaceShip,EnemySpaceShips,RocketShip,FlyingSaucer
from black_hole import BlackHole
from strength import Strength
from red_button import RedButton
from wildcard import WildCard


from moon import Moon
from coin import Coin


clock = pygame.time.Clock()
title = "SPACE INVADERS"
pygame.display.set_caption(title)


WHITE = (255,255,255)
RED = (255,0,0)


background_image = pygame.image.load(os.path.join('assets','bg.png'))

def game():
    
    
    high_score_file_name = "high_scores.txt"

    with open(high_score_file_name,'r') as f:
        high_scores = list(map(int,f.readlines()))
    

    def update_high_scores_if_necessary(score):

        if score > high_scores[-1]:
            high_scores.pop()
            high_scores.append(score)
            high_scores.sort(reverse=True)

            with open(high_score_file_name,'w') as f:
                for high_score in high_scores:
                    f.write(str(high_score) + '\n')
        
    
    coin_image = pygame.image.load(os.path.join('assets','gold_coin_animation','gold_coin_round_blank_1.png')).convert_alpha()
    coin_size = 20
    coin_image = pygame.transform.scale(coin_image,(coin_size,coin_size))
    coin_font = pygame.font.Font(os.path.join('assets','atari.ttf'),20)
    def draw_coins_collected_topleft():
        topleft = (5,5)
        screen.blit(coin_image,topleft)
        coin_text = coin_font.render(str(player_ship.sprite.coins_collected),True,WHITE)
        screen.blit(coin_text,(10 + coin_image.get_width(),5))









    def reset():
        nonlocal player_ship,aliens,game_over,started,seconds,seconds_text,start_time,second_text_rect,wave,wave_text,time_text,time_text_rect,time_passed
        wave = 1
        wave_text = wave_font.render(f"WAVE: {wave}",True,WHITE)
        player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
        aliens = Aliens(WIDTH)
        enemy_ships.empty()
        items.empty()
        enemy_objects.empty()
        #for sprite in items:
            #sprite.kill()
        started = False
        game_over = False
        #seconds =3
        seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
        second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
        time_passed =0
        time_text = second_font.render(str(time_passed),True,WHITE)
        time_text_rect = time_text.get_rect(center=(WIDTH//2,second_top_gap + time_text.get_height()//2))
        start_time = time.time()
        start_sound.play()

    font = pygame.font.Font(os.path.join('assets','atari.ttf'),30)
    game_over_text = font.render("GAME OVER!",True,WHITE)
    gap_from_center = 50
    game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
    

    wave = 1
    wave_font = pygame.font.Font(os.path.join('assets','atari.ttf'),20)
    wave_text = wave_font.render(f"WAVE: {wave}",True,WHITE)
    wave_text_rect= wave_text.get_rect(topright=(WIDTH-10,10))

    

    item_types = [Heart,InvincibilityPotion,Cross,Star,TorpedoPowerUp,Safety,Skull,BombPowerUp,Snowflake,PoisonMuk,BombPowerUp,Strength,RedButton,'wildcard',Safety,InvincibilityPotion]
    buttons_gap_from_edge = 100

    play_again_text = font.render("PLAY AGAIN",True,WHITE)
    play_again_surface = pygame.Surface((play_again_text.get_width() + 50,play_again_text.get_height() + 50),pygame.SRCALPHA)
    play_again_surface.fill(RED)

    play_again_surface.blit(play_again_text,(play_again_surface.get_width()//2 - play_again_text.get_width()//2,play_again_surface.get_width()//2 - play_again_text.get_width()//2))
    play_again_surface_rect = play_again_surface.get_rect(center=(WIDTH//2,game_over_text_rect.bottom + 100))

    menu_text = font.render("MENU",True,WHITE)
    menu_surface = pygame.Surface((menu_text.get_width() + 50,menu_text.get_height() + 50),pygame.SRCALPHA)
    menu_surface.fill(RED)

    menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_width()//2 - menu_text.get_width()//2))
    menu_surface_rect = menu_surface.get_rect(center=(WIDTH//2,play_again_surface_rect.bottom + 100))


    alpha_play_again_text_surface = pygame.Surface(play_again_text.get_size(),pygame.SRCALPHA)
    alpha_play_again_text_surface.fill((255,0,0,128))

    pygame.mixer.music.load(os.path.join('assets','level1.ogg'))

    start_sound = pygame.mixer.Sound(os.path.join('assets','racestart.wav'))

    player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
    aliens = Aliens(WIDTH)

    explosions = pygame.sprite.Group()
    hearts = pygame.sprite.Group()
    potions = pygame.sprite.Group()
    items = pygame.sprite.Group()
    crosses = pygame.sprite.Group()



    ships = EnemySpaceShips()

    game_over = False
    topleft=(0,0)
    red_transparent = (255,0,0,128)    
    started = False

    texts = ["READY!","SET!","GO!"]
    seconds = 3
    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))

    game_over_music = pygame.mixer.Sound(os.path.join('assets','Retro_No hope.ogg'))

    def display(wave):
        
        topleft = (0,0)
        
        wave_font = pygame.font.Font(os.path.join('assets','atari.ttf'),50)
        gap = 50
        wave_text_1 = font.render("WAVE",True,WHITE)
        wave_text_2 = font.render(str(wave),True,WHITE)
        wave_text_1_rect = wave_text_1.get_rect(center=(WIDTH//2,HEIGHT//2))
        wave_text_2_rect = wave_text_2.get_rect(center=(WIDTH//2,wave_text_1_rect.bottom + gap))

        
        SECOND_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SECOND_EVENT,1000)
        seconds = 3
        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == SECOND_EVENT:
                    seconds -= 1
                    if seconds == 0:
                        pygame.time.set_timer(SECOND_EVENT,0)
                        return
            
            explosions.update()
            screen.blit(background_image,topleft)
            screen.blit(wave_text_1,wave_text_1_rect)
            screen.blit(wave_text_2,wave_text_2_rect)

            pygame.display.update()
            clock.tick(FPS)
    

    second_font = pygame.font.SysFont(os.path.join('assets','atari.ttf'),30)

    HEART_EVENT = pygame.USEREVENT + 2
    milliseconds =2000 #10000
    pygame.time.set_timer(HEART_EVENT,2000)
    ENEMY_SHIP_EVENT = pygame.USEREVENT + 5
    pygame.time.set_timer(ENEMY_SHIP_EVENT,15000)
    ENEMY_OBJECT_EVENT = pygame.USEREVENT + 7
    pygame.time.set_timer(ENEMY_OBJECT_EVENT,7000)

    COIN_EVENT = pygame.USEREVENT + 10
    milliseconds = 5000
    pygame.time.set_timer(COIN_EVENT,milliseconds)

    enemy_objects = pygame.sprite.Group()

    display(wave)
    start_time = time.time()
    start_sound.play()
    
    time_passed = 0
    

    time_text = second_font.render(str(time_passed),True,WHITE)
    second_top_gap = 10
    time_text_rect = time_text.get_rect(center=(WIDTH//2,second_top_gap + time_text.get_height()//2))
    enemy_ships = pygame.sprite.Group()
    enemy_ship_types = [RocketShip,EnemySpaceShip]
    while True:

        

        current_time = time.time()

        if not started:
            if current_time - start_time >= 1:
                seconds -= 1
                if seconds == 0:
                    started = True
                    pygame.mixer.music.play(-1)
                    seconds = 3
                    start_time = current_time
                else:
                    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
                    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
                    start_time = current_time
        elif not game_over:
            if current_time - start_time >= 1:
                time_passed += 1
                time_text = second_font.render(str(time_passed),True,WHITE)
                time_text_rect = time_text.get_rect(center=(WIDTH//2,second_top_gap + time_text.get_height()//2))
                start_time = current_time





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                if play_again_surface_rect.collidepoint(point):
                    game_over_music.stop()
                    reset()
                elif menu_surface_rect.collidepoint(point):
                    game_over_music.stop()
                    return
            elif started and not game_over:
                if event.type == HEART_EVENT:
                    if random.randint(1,25) == 1:
                        item = Cross(WIDTH,HEIGHT)
                        items.add(item)
                    else:
                        number = random.randint(len(item_types) - 1,len(item_types) -1)
                        class_ =item_types[number] 
                        hidden = False
                        if class_ == 'wildcard':
                            class_ = random.choice([Strength,RedButton,InvincibilityPotion,Safety,TorpedoPowerUp,BombPowerUp])
                            hidden= True
                        item = class_(WIDTH,HEIGHT,hidden=hidden)
                        items.add(item)
                elif event.type == ENEMY_SHIP_EVENT:
                    ship_class= random.choice(enemy_ship_types)
                    enemy = FlyingSaucer(WIDTH,HEIGHT,speed=3)
                    enemy_ships.add(enemy)
                elif event.type == ENEMY_OBJECT_EVENT:
                    meteor = BlackHole(WIDTH,HEIGHT)
                    #enemy_ships.add(meteor)
                    enemy_objects.add(meteor)


                elif event.type == COIN_EVENT:
                    coin = Coin(WIDTH,HEIGHT)
                    items.add(coin)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if player_ship.sprite.has_torpedo:
                            player_ship.sprite.fire_torpedo()
                        elif player_ship.sprite.has_bomb:
                            player_ship.sprite.fire_bomb()
                    elif player_ship.sprite.poisoned and player_ship.sprite.coins_collected >= 5 and event.key == pygame.K_j:
                        player_ship.sprite.unpoison()
                        player_ship.sprite.removeCoins(5)
                elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                    player_ship.sprite.release_bomb()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                start_sound.stop()
                game_over_music.stop()
                return



        
        
        explosions.update()
        if started and not game_over:
            items.update()
            #hearts.update()
            pressed_keys = pygame.key.get_pressed()
            aliens.update()
            ships.update()
            enemy_objects.update()
            enemy_ships.update()
            game_over = player_ship.sprite.update(pressed_keys,aliens.get_group(),aliens.get_bullets(),explosions,hearts,potions,crosses,items,enemy_ships,enemy_objects) 
            if game_over:
                pygame.mixer.music.stop()
                game_over_music.play()
                update_high_scores_if_necessary(wave -1)
            if aliens.is_empty():
                wave += 1
                update_high_scores_if_necessary(wave -1)
                wave_text = wave_font.render(f"WAVE: {wave}",True,WHITE)
                player_ship.sprite.restore_health_and_remove_bullets()
                #for sprite in items:
                    #sprite.kill()
                aliens.reset()
                hearts.empty()
                items.empty()
                potions.empty()
                started = False
                time_passed =0
                time_text = second_font.render(str(time_passed),True,WHITE)
                time_text_rect = time_text.get_rect(center=(WIDTH//2,second_top_gap + time_text.get_height()//2))
                display(wave)
                start_sound.play()
                seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
                start_time = time.time()


        screen.blit(background_image,topleft)
        for enemy_object in enemy_objects:
            enemy_object.draw(screen)
        for enemy_ship in enemy_ships:
            enemy_ship.draw(screen)

        items.draw(screen)
        #hearts.draw(screen)
        aliens.draw(screen)
        if player_ship:
            player_ship.sprite.draw(screen)
            draw_coins_collected_topleft()
            player_ship.sprite.draw_health_bar_and_bullets(screen)
        explosions.draw(screen)
        screen.blit(wave_text,wave_text_rect)
        screen.blit(time_text,time_text_rect)


        if not started:
            screen.blit(seconds_text,second_text_rect)
        elif game_over:

            point = pygame.mouse.get_pos()

            if play_again_surface_rect.collidepoint(point):
                play_again_surface.fill(red_transparent)
                play_again_surface.blit(play_again_text,(play_again_surface.get_width()//2 - play_again_text.get_width()//2,play_again_surface.get_width()//2 - play_again_text.get_width()//2))
            else:
                play_again_surface.fill(RED)
                play_again_surface.blit(play_again_text,(play_again_surface.get_width()//2 - play_again_text.get_width()//2,play_again_surface.get_width()//2 - play_again_text.get_width()//2))
            

            if menu_surface_rect.collidepoint(point):
                menu_surface.fill(red_transparent)

                menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_width()//2 - menu_text.get_width()//2))
            else:
                menu_surface.fill(RED)

                menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_width()//2 - menu_text.get_width()//2))



            screen.blit(game_over_text,game_over_text_rect)
            screen.blit(play_again_surface,play_again_surface_rect)
            screen.blit(menu_surface,menu_surface_rect)
        

        pygame.display.update()
        clock.tick(FPS)


def high_score_screen():
    

    file_name = "high_scores.txt"


    with open(file_name,'r') as f:
        scores = list(map(int,f.readlines()))
    
    
    scores_font = pygame.font.Font(os.path.join('assets','atari.ttf'),20)


    




    high_scores_font = pygame.font.Font(os.path.join('assets','atari.ttf'),40)
    topleft= (0,0)
    
    top_gap = 50
    high_scores_text = high_scores_font.render("HIGH SCORES",True,WHITE)
    
    
    transparent_red = (255,0,0,128)
    menu_text = high_scores_font.render("MENU",True,WHITE)
    menu_surface = pygame.Surface((menu_text.get_width() + 50,menu_text.get_height() + 50),pygame.SRCALPHA)
    menu_surface.fill(RED)
    menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_height()//2 - menu_text.get_height()//2))
    menu_surface_rect = menu_surface.get_rect(center=(WIDTH//2,HEIGHT - 50 - menu_surface.get_height()//2))
    

    def draw_scores():
        screen.blit(background_image,topleft)
        screen.blit(high_scores_text,(WIDTH//2 - high_scores_text.get_width()//2,top_gap))
        gap_between = 90
        gap_between_scores= 40
        width = len(str(scores[0]))
        for i in range(5):
            score = scores[i]
            score_text = high_scores_font.render(f"{i + 1}. {str(score)}",True,WHITE)
            screen.blit(score_text,(gap_between,top_gap * 3 + (gap_between_scores + score_text.get_height()) * i))
        
        
        first_width = None
        for i in range(5,len(scores)):
            score = scores[i]
            score_text = high_scores_font.render(f"{i +1:>2}. {str(score)}",True,WHITE)
            if first_width is None:
                first_width = score_text.get_width()
            screen.blit(score_text,(WIDTH - gap_between - first_width,top_gap * 3 + (gap_between_scores + score_text.get_height()) * (i - 5)))
        
        screen.blit(menu_surface,menu_surface_rect)
        pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()

                if menu_surface_rect.collidepoint(point):
                    return

        

        point = pygame.mouse.get_pos()

        if menu_surface_rect.collidepoint(point):
            menu_surface.fill(transparent_red)
            menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_height()//2 - menu_text.get_height()//2))
        else:
            menu_surface.fill(RED)
            menu_surface.blit(menu_text,(menu_surface.get_width()//2 - menu_text.get_width()//2,menu_surface.get_height()//2 - menu_text.get_height()//2))





         



        
        draw_scores()


def power_up_screen():
    
    

    def load_items():

        
        
        item_types = [Heart,InvincibilityPotion,Cross,Star,TorpedoPowerUp,Safety,Skull,BombPowerUp,Snowflake,PoisonMuk,FreeMovement,Strength,RedButton]
        
        item_type_index = 0

        items_group = pygame.sprite.Group() 

    
        top_gap = 450
            
        gap_between_items = 20
        rows = 5
        size = 40
        side_gap = (WIDTH - (size + gap_between_items) * rows)//2
        print(len(item_types)/rows)
        for row in range(math.ceil(len(item_types)/rows)):
            for col in range(rows):
                item = item_types[item_type_index](WIDTH,HEIGHT)

                x= side_gap + (col * (size + gap_between_items))
                y= top_gap + (row * (size + gap_between_items))
                item.change_rects_topleft(x,y)
                item_type_index += 1

                items_group.add(item)
                if item_type_index == len(item_types):
                    break

            else:
                continue

            break

            


        return items_group






    




    items_group = load_items()
        



    

    font_path = os.path.join('assets','atari.ttf')
    title_font_size = 40
    

    text_group = pygame.sprite.Group()
    hover_font_size = 20
    title_text = Text("ITEMS",WIDTH//2,50,font_path,title_font_size,WHITE,center_coordinate=True)
    hover_text = Text("HOVER OVER ITEMS FOR DETAILS",WIDTH//2,100,font_path,hover_font_size,WHITE,center_coordinate=True)

    text_group.add(title_text)
    text_group.add(hover_text)
    menu_button = Button("BACK",WIDTH//2,HEIGHT - 100,WHITE,RED,None,title_font_size)

    
    button_group = pygame.sprite.Group(menu_button)



    

    while True:

        

        text = None
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()

                for button in button_group:
                    if button.clicked_on(point):
                        if button.callback:
                            button.callback()
                        else:
                            return


        screen.blit(background_image,(0,0))
        

        point = pygame.mouse.get_pos()


        for item in items_group:
            if item.is_hovered_on(point):
                text = item.text


        
        if text:
            if isinstance(text,list):
                start = 150
                for i,t in enumerate(text):
                    screen.blit(t,(WIDTH//2 - t.get_width()//2,150 + (i * (t.get_height() + 20))))
            else:
                screen.blit(text,(WIDTH//2- text.get_width()//2,150))



        button_group.update(point)
        

        items_group.draw(screen)
        text_group.draw(screen)
        button_group.draw(screen)

        pygame.display.update()


def enemies_screen():
    
    topleft = (0,0)
    screen.blit(background_image,topleft)
    font_path = os.path.join('assets','atari.ttf')
    title_font_size = 40
    title_text = Text("ENEMIES",WIDTH//2,50,font_path,title_font_size,WHITE,center_coordinate=True)
    menu_button = Button("BACK",WIDTH//2,HEIGHT - 100,WHITE,RED,None,title_font_size)
        
    button_group = pygame.sprite.Group(menu_button)
    text = pygame.sprite.GroupSingle(title_text)
    
    
    class Icon(pygame.sprite.Sprite):


        def __init__(self,x,y,image,size=40):
            super().__init__()

            if type(image) == list:
                self.images = image
                for i,image in enumerate(self.images):
                    self.images[i] = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(size,size))

                self.image = self.images[0]
                self.multiple = True
            else:
                self.image = pygame.transform.scale(image,(size,size))
                self.multiple = False



            self.rect = self.image.get_rect(topleft=(x,y))



    class MultipleIcon(pygame.sprite.Sprite):


        def __init__(self,x,y,images,size=-1,frames=60):
            super().__init__()
            self.images = images

            
            for i,image in enumerate(self.images):
                if size != -1:
                    self.images[i] = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(size,size))
                else:
                    self.images[i] = pygame.image.load(image).convert_alpha()

            self.image = self.images[0]

            self.rect = self.image.get_rect(topleft=(x,y))
            self.image_index = 0
            self.frame_counter = 0
            self.frames = frames


        def update(self):


            self.frame_counter += 1

            if self.frame_counter == self.frames:
                self.frame_counter = 0
                self.image_index = (self.image_index + 1) % len(self.images)

                self.image = self.images[self.image_index]



    image_size = 60
    top_gap = HEIGHT//2 + 50

    icons = pygame.sprite.Group()
    


    cols = 4
    rows = 2

    gap = 40
    left_gap = WIDTH//2  - ((image_size + gap) *cols - gap)//2

    
    directory = os.path.join('assets','aliens')

    file_names = [os.path.join(directory,file_name) for file_name in os.listdir(directory)]
    images = [file_names]
    print(len(file_names))

    directory = os.path.join('assets','enemies')

    images = []
    for file_ in os.listdir(directory):
        path = os.path.join(directory,file_)
        if os.path.isfile(path):
            images.append(path)
        else:
            file_names = [os.path.join(path,file_name) for file_name in os.listdir(path)]
            images.append(file_names)
    
    exit = False
    for row in range(rows):
        for col in range(cols):
            try:
                image = images[row * cols + col]
            except IndexError:
                exit = True
                break

            


            if isinstance(image,list):
                if row * cols + col > 1:
                    fps = 10
                else:
                    fps = 60

                icon = MultipleIcon(left_gap + (col * (image_size + gap)),top_gap +row * image_size,image,image_size,fps)
            else:
                icon = Icon(left_gap + (col * (image_size + gap)),top_gap +row * image_size,image,image_size)
            icons.add(icon)
        if exit:
            break


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                for button in button_group:
                    if button.clicked_on(point):
                        if button.callback:
                            button.callback()
                        else:
                            return

        
        screen.blit(background_image,topleft)
         
        point = pygame.mouse.get_pos()
        button_group.update(point)
        icons.update()

        text.draw(screen)
        

        button_group.draw(screen)
        icons.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



def instructions_screen():
    
    
    text_group = pygame.sprite.Group()
    
    font_path = os.path.join('assets','atari.ttf')
    title_font_size = 40

    title_text = Text("HOW TO PLAY",WIDTH//2,50,font_path,title_font_size,WHITE,center_coordinate=True)
    
    
    instructions = "HIT SPACEBAR TO FIRE MISSILES TOWARDS ENEMIES. USE THE LEFT AND RIGHT ARROW TO MOVE LEFT AND RIGHT. COLLECT POWERUPS FOR BOOSTS AND AVOIDTHE HARMFUL ITEMS. DEFEAT A WAVE TO MOVE ON TO THE NEXT ONE."

    width = 28
    texts = textwrap.wrap(instructions,width)

    gap = 40
    start = 50 + title_text.get_height()//2 +  gap
    instruction_font_size = 20
    gap = 20
    for i,text in enumerate(texts):
        text_sprite = Text(text,WIDTH//2,start + i * (instruction_font_size + 20),font_path,instruction_font_size,WHITE,center_coordinate=True)
        text_group.add(text_sprite)
    




    text_group.add(title_text)
    screen.blit(background_image,(0,0))

    menu_button = Button("MENU",WIDTH//2,HEIGHT - 100,WHITE,RED,None,title_font_size)
    power_ups_button = Button("ITEMS",WIDTH//2,HEIGHT - 220,WHITE,RED,power_up_screen,title_font_size)
    enemies_button = Button("ENEMIES",WIDTH//2,HEIGHT - 340,WHITE,RED,enemies_screen,title_font_size)


    button_group = pygame.sprite.Group(menu_button,power_ups_button,enemies_button)
    


    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                

                for button in button_group:
                    if button.clicked_on(point):
                        if button.callback:
                            button.callback()
                        else:
                            return



        point = pygame.mouse.get_pos()
        button_group.update(point)
        screen.blit(background_image,(0,0))
        

        text_group.draw(screen)
        button_group.draw(screen)

        pygame.display.update()



def menu():
    title_font = pygame.font.Font(os.path.join('assets','atari.ttf'),40)
    top_gap = 50
    title_text = title_font.render("SPACE INVADERS",True,WHITE)
    
    
    def load_moon_images():
        directory = os.path.join('assets','hjm-moon')

        moon_images = []
        for file_ in os.listdir(directory):
            moon_image = pygame.image.load(os.path.join(directory,file_)).convert_alpha()
            moon_images.append(moon_image)

        return moon_images



    



    transparent_red = (255,0,0,128)

    high_scores_text = title_font.render("HIGH SCORES",True,WHITE)

    high_scores_text_surface = pygame.Surface((high_scores_text.get_width() + 50,high_scores_text.get_height() + 50),pygame.SRCALPHA)
    high_scores_text_rect = high_scores_text.get_rect(center=(high_scores_text_surface.get_width()//2,high_scores_text_surface.get_height()//2))
     
    high_scores_text_surface.fill(RED)
    high_scores_text_surface_rect = high_scores_text_surface.get_rect(center=(WIDTH//2,HEIGHT - top_gap - high_scores_text_surface.get_height()//2))
    high_scores_text_surface.blit(high_scores_text,high_scores_text_rect)


    alpha_high_score_text_surface = pygame.Surface(high_scores_text.get_size(),pygame.SRCALPHA)
    alpha_high_score_text_surface.fill((255,0,0,128))


    title_text_rect= title_text.get_rect(center=(WIDTH//2,top_gap + title_text.get_height()//2))
    
    enter_font = pygame.font.Font(os.path.join('assets','atari.ttf'),30)
    enter_text = enter_font.render("Hit ENTER To Play!",True,WHITE)
    enter_text_rect = enter_text.get_rect(center=(WIDTH//2,HEIGHT//2))
    topleft = (0,0)
    pygame.mixer.music.load(os.path.join('assets','intro.ogg'))
    pygame.mixer.music.play(-1)
    
    alpha_surface = pygame.Surface(enter_text.get_size(),pygame.SRCALPHA)
    alpha = 255
    
    title_font_size = 40

    moon = Moon(WIDTH//2,title_text_rect.bottom + 150)
    moon = pygame.sprite.GroupSingle(moon)
    

    buttons = pygame.sprite.Group()
    button_1 = Button("HOW TO PLAY",WIDTH//2,high_scores_text_surface_rect.top - 100,WHITE,RED,instructions_screen,title_font_size)
    button_2 = Button("HIGH SCORES",WIDTH//2,HEIGHT - top_gap - 50,WHITE,RED,high_score_screen,title_font_size)
    buttons.add(button_1)
    buttons.add(button_2)
        
    MOON_CHANGE_EVENT = pygame.USEREVENT + 4
    milliseconds = 200
    pygame.time.set_timer(MOON_CHANGE_EVENT,milliseconds)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    game()
                    pygame.mixer.music.load(os.path.join('assets','intro.ogg'))
                    pygame.mixer.music.play(-1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                
                for button in buttons:
                    if button.clicked_on(point):
                        button.callback()
                #if high_scores_text_surface_rect.collidepoint(point):
                    #high_score_screen()
            elif event.type == MOON_CHANGE_EVENT:
                moon.update()

         
        
        if alpha > 0:
            alpha = max(alpha - 4,0)
            enter_text_copy = enter_text.copy()
            alpha_surface.fill((255,255,255,alpha))
            enter_text_copy.blit(alpha_surface,(0,0),special_flags=pygame.BLEND_RGBA_MULT)
        else:
            alpha = 255

        
        point = pygame.mouse.get_pos()
        if high_scores_text_surface_rect.collidepoint(point):
            high_scores_text_surface.fill(transparent_red)
            high_scores_text_surface.blit(high_scores_text,high_scores_text_rect)
        else:
            high_scores_text_surface.fill(RED)
            high_scores_text_surface.blit(high_scores_text,high_scores_text_rect)

        
        buttons.update(point)

        
        screen.blit(background_image,topleft)
        

        moon.draw(screen)
        screen.blit(title_text,title_text_rect)
        screen.blit(enter_text_copy,enter_text_rect)

        #screen.blit(high_scores_text_surface,high_scores_text_surface_rect)
        buttons.draw(screen)
        pygame.display.update()




if __name__ == "__main__":
    
    menu()



