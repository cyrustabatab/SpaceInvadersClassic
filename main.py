import pygame,sys,os,time
pygame.init()

WIDTH,HEIGHT = 600,800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))

from spaceship import Spaceship
from aliens import Aliens

clock = pygame.time.Clock()
title = "SPACE INVADERS"
pygame.display.set_caption(title)




WHITE = (255,255,255)
RED = (255,0,0)


background_image = pygame.image.load(os.path.join('assets','bg.png'))

def game():
    


    def reset():
        nonlocal player_ship,aliens,game_over,started,seconds,seconds_text,start_time,second_text_rect
        player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
        aliens = Aliens(WIDTH)
        started = False
        game_over = False
        seconds =3
        seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
        second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
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

    game_over = False
    topleft=(0,0)
    red_transparent = (255,0,0,128)    
    started = False

    start_time = time.time()
    seconds =3
    texts = ["READY!","SET!","GO!"]
    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
    start_sound.play()

    while True:
        

        if not started:
            current_time = time.time()
            if current_time - start_time >= 1:
                seconds -= 1
                if seconds == 0:
                    started = True
                    pygame.mixer.music.play(-1)
                else:
                    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
                    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
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

        
        explosions.update()
        if started and not game_over:
            pressed_keys = pygame.key.get_pressed()
            aliens.update()
            game_over = player_ship.sprite.update(pressed_keys,aliens.get_group(),aliens.get_bullets(),explosions) 
        screen.blit(background_image,topleft)
        aliens.draw(screen)
        player_ship.draw(screen)
        explosions.draw(screen)
        screen.blit(wave_text,wave_text_rect)
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


def menu():
    title_font = pygame.font.Font(os.path.join('assets','atari.ttf'),40)
    top_gap = 50
    title_text = title_font.render("SPACE INVADERS",True,WHITE)
    

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

         
        
        if alpha > 0:
            alpha = max(alpha - 4,0)
            enter_text_copy = enter_text.copy()
            alpha_surface.fill((255,255,255,alpha))
            enter_text_copy.blit(alpha_surface,(0,0),special_flags=pygame.BLEND_RGBA_MULT)
        else:
            alpha = 255


        
        screen.blit(background_image,topleft)

        screen.blit(title_text,title_text_rect)
        screen.blit(enter_text_copy,enter_text_rect)
        pygame.display.update()




if __name__ == "__main__":
    
    menu()



