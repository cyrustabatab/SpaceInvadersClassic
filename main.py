import pygame,sys,os,time,random
pygame.init()

WIDTH,HEIGHT = 600,800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))

from spaceship import Spaceship
from aliens import Aliens
from heart import Heart
from potion import InvincibilityPotion
from cross import Cross

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



    def reset():
        nonlocal player_ship,aliens,game_over,started,seconds,seconds_text,start_time,second_text_rect,wave,wave_text,time_text,time_text_rect,time_passed
        wave = 1
        wave_text = wave_font.render(f"WAVE: {wave}",True,WHITE)
        player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
        aliens = Aliens(WIDTH)
        for sprite in items:
            sprite.kill()
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

    game_over = False
    topleft=(0,0)
    red_transparent = (255,0,0,128)    
    started = False

    texts = ["READY!","SET!","GO!"]
    seconds = 3
    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
    
    



    

    

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
    milliseconds = 10000
    pygame.time.set_timer(HEART_EVENT,10000)



    display(wave)
    start_time = time.time()
    start_sound.play()
    
    time_passed = 0

    time_text = second_font.render(str(time_passed),True,WHITE)
    second_top_gap = 10
    time_text_rect = time_text.get_rect(center=(WIDTH//2,second_top_gap + time_text.get_height()//2))
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
                    reset()
                elif menu_surface_rect.collidepoint(point):
                    return
            elif started and not game_over and event.type == HEART_EVENT:
                if random.randint(1,50) == 1:
                    item = Cross(WIDTH)
                    crosses.add(item)
                elif random.randint(1,2) == 1:
                    x,y=random.randint(0,WIDTH - 20),random.randint(-20,-10)
                    item = Heart(x,y)
                    hearts.add(item)
                else:
                    item = InvincibilityPotion(WIDTH)
                    potions.add(item)
                items.add(item)

        
        
        explosions.update()
        if started and not game_over:
            items.update()
            #hearts.update()
            pressed_keys = pygame.key.get_pressed()
            aliens.update()
            game_over = player_ship.sprite.update(pressed_keys,aliens.get_group(),aliens.get_bullets(),explosions,hearts,potions,crosses) 
            if game_over:
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
        items.draw(screen)
        #hearts.draw(screen)
        aliens.draw(screen)
        if player_ship:
            player_ship.sprite.draw(screen)
        explosions.draw(screen)
        screen.blit(wave_text,wave_text_rect)
        screen.blit(time_text,time_text_rect)
        if  not game_over:
            player_ship.sprite.draw_health_bar_and_bullets(screen)

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
def menu():
    title_font = pygame.font.Font(os.path.join('assets','atari.ttf'),40)
    top_gap = 50
    title_text = title_font.render("SPACE INVADERS",True,WHITE)
    

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

                if high_scores_text_surface_rect.collidepoint(point):
                    high_score_screen()

         
        
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




        
        screen.blit(background_image,topleft)

        screen.blit(title_text,title_text_rect)
        screen.blit(enter_text_copy,enter_text_rect)

        screen.blit(high_scores_text_surface,high_scores_text_surface_rect)
        pygame.display.update()




if __name__ == "__main__":
    
    menu()



