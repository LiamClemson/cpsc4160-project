#IMPORT STATEMENTS
import pygame, sys, os
import time
from models import *
from images import *
import pygame.freetype

from model_implementation import *

"""
NOTES



CONCEPTS:

driftwood to heal boat / shipwrecks to damage boat
speed / health bonuses
speed decrements/limited depending on ship health
ship health system: 50
enemy damage to ship: 10
obstacle damage to ship: 5
speed limitations: 30-50:3, 20-30:2, 0-20:1
speed bonus: 1
health bonus: 15

Major Oceans:
Panthalassa
Paleo-Tethys

Marine Life:
bryozoa
brachiopods
ammonoids
echinoderms (most crinoids)
chondrichthyes
Mollusca
Nautiloid cephalopods
goniatite ammonoids
trilobites (rare)
ostracods

elasmobranchs (psamodus, symmoriida, petalodonts, xenacanthida)

bony fish (palaeonisciformes)
sarcopterygian
rhizodonts

ctenodus, uronemus, acanthodes, cheirodus, gyracanthus


"""

#CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0, 51, 102)

ORANGE = (255, 165, 0)
PURPLE = (230,230,250)

#SET UP
pygame.display.set_caption("gone fishing")
clock = pygame.time.Clock()

#INITIALIZATION STATEMENT
pygame.init()

#TEXT SETTINGS
display_font = pygame.font.SysFont('goudyoldstyle', 20)
global period_text
global clock_font
clock_font = pygame.font.SysFont('goudyoldstyle', 20)
period_text = display_font.render('CAMBRIAN PERIOD     | NEXT PERIOD: 485 MYA |', True, (255, 255, 255))
global player_health_text
#player_health_text = display_font.render('Health: ' + str(player.health), True, (255, 255, 255))
global player_speed_text
#player_speed_text = display_font.render('Speed: ' + str(player.speed), True, (255, 255, 255))
global player_score_text
#player_score_text = display_font.render('Score: ' + str(player.score), True, (255, 255, 255))
global player_net_text
#player_net_text = display_font.render('Animals Caught: ' + str(player.net), True, (255, 255, 255))
global clock_text_color
clock_text_color = (255, 255, 255)
clock_text = clock_font.render('0', True, clock_text_color)

#TIME SETTINGS
clock_enabled = True
global pause
global game_pause
global player_action
game_pause = False
pause = False
player_action = False
def paused(screen, current_time, player_action):
    global play_ocean_sound
    global curr_period
    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text
    play_ocean_sound = True
    pygame.mixer.music.pause()
    global pause
    pause = True
    pause_font = pygame.font.SysFont('Camrbia', 150)
    continue_font = pygame.font.SysFont('Camrbia', 25)
    if player_action:
        pause_text = pause_font.render('PAUSED', True, (255, 255, 255))
        continue_text = continue_font.render('[ PRESS \'P\' TO CONTINUE FISHING ]', True, (255, 255, 255))

        screen.blit(clock_text, (1, 20))
        screen.blit(period_text, (1, 1))
        screen.blit(player_health_text, (1,45))
        screen.blit(player_speed_text, (1,65))
        screen.blit(player_net_text, (SCREEN_WIDTH - 210,1))
        screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
        screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
        screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
        screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
        screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
        screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))
        player.update(screen)
        if curr_period >= 1:
            enemy.update(screen)
        buoyObstacle.update(current_time, screen, buoyobstacle1)
        buoyObstacle2.update(current_time, screen, buoyobstacle2)
        fishArea1.update(screen, current_time)
        fishArea2.update(screen, current_time)
        fishArea3.update(screen, current_time)
        fishArea4.update(screen, current_time)
        fishArea5.update(screen, current_time)

        screen.blit(pause_text, (SCREEN_WIDTH/2 - (pause_text.get_width()/2), SCREEN_HEIGHT/2))
        screen.blit(continue_text, (SCREEN_WIDTH/2 - (continue_text.get_width()/2), SCREEN_HEIGHT/2 + 100))

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
        
        pygame.display.update()
        clock.tick(40)

def compact_text(screen, text, pos, font, font_color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x, y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, font_color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= SCREEN_WIDTH:
                x = pos[0]
                y += word_height
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

def main_menu():
    pygame.mixer.music.load('shoreline.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    waiting = True
    menu = True
    instructions = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and menu == True:
                    pygame.mixer.music.stop()
                    waiting = False
                if event.key == pygame.K_f:
                    instructions = True
                    if instructions:
                        screen.fill((255, 255, 255))
                        menu = False
                        text = 'HOW TO PLAY:\n'
                        text += 'press and hold WASD or the ARROW KEYS to move the boat\n'
                        text += 'press SPACEBAR to toggle the fishing action\n'
                        text += 'toggle the fishing action to \'on\' while floating over ripples to fish\n'
                        text += 'be patient! it may take several seconds before catching something\n'
                        text += 'rapidly toggling the fishing action will delay the fishing process\n\n'
                        text += 'HOW TO WIN:\n'
                        text += 'survive until the end of the game\n'
                        text += 'the goal is to accumulate as many points at possible by the end\n'
                        text += 'successfully fishing will improve your score\n'
                        text += 'avoid hazards in the water to prevent the boat from taking damage\n'
                        text += 'collect power-ups to improve boat health and speed\n\n'
                        text += 'TIPS:\n'
                        text += 'when being shown an \'information\' screen related to a time period or animal dont rush!\n'
                        text += 'game time will automatically pause on these screens to allow you time to read\n'
                        text += 'you won\'t lose any precious fishing time!\n\n'
                        text += '[ PRESS \'G\' TO RETURN TO MENU ]'
                        screen.blit(art_credit_text, (SCREEN_WIDTH - art_credit_text.get_width(), SCREEN_HEIGHT - art_credit_text.get_height()))
                        compact_text(screen, text, (5,5), menu_font, (0,0,0))
                if event.key == pygame.K_g:
                    menu = True
                    instructions = False

        if menu:
            screen.fill((255, 255, 255))
            title_font = pygame.font.SysFont('Camrbia', 75)
            menu_font = pygame.font.SysFont('Camrbia', 25)
            title_text = title_font.render('Paleo Fisher', True, (0,0,0))
            continue_text = menu_font.render('[ PRESS \'ENTER\' TO WARP THROUGH TIME AND SET SAIL! ]', True, (0,0,0))
            how_to_play_text = menu_font.render('[ PRESS \'F\' FOR INSTRUCTIONS ]', True, (0,0,0))
            art_credit_text = menu_font.render('Animal Art Director: Ryan Madden ', True, (0,0,0))
            screen.blit(title_text, (SCREEN_WIDTH/2 - (title_text.get_width()/2), SCREEN_HEIGHT/5))
            screen.blit(how_to_play_text, (SCREEN_WIDTH/2 - (how_to_play_text.get_width()/2), SCREEN_HEIGHT/5 + (title_text.get_height())))
            screen.blit(continue_text, (SCREEN_WIDTH/2 - (continue_text.get_width()/2), SCREEN_HEIGHT/5 + (title_text.get_height() + continue_text.get_height())))
            screen.blit(art_credit_text, (SCREEN_WIDTH - art_credit_text.get_width(), SCREEN_HEIGHT - art_credit_text.get_height()))
        pygame.display.update()
        clock.tick(40)  

def game_paused(animal_screen):
    global play_ocean_sound
    pygame.mixer.music.pause()
    if animal_screen:
        pygame.mixer.music.load('pirateship.wav')
        pygame.mixer.music.play(-1)
    play_ocean_sound = True
    global game_pause
    game_pause = True
    while game_pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if animal_screen:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.Sound.stop(clock_chime_sound)
                        pygame.mixer.Sound.stop(sea_creature_sound)
                        pygame.mixer.Sound.stop(crash_wood_sound)
                        game_pause = False
                else:
                    if event.key == pygame.K_f:
                        pygame.mixer.Sound.stop(clock_chime_sound)
                        game_pause = False
        
        pygame.display.update()
        clock.tick(40)  

def count_down():
    global curr_period
    wait = True
    time_0 = time.time()
    count = 3
    count_font = pygame.font.SysFont('Camrbia', 150)
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        count_text = count_font.render(str(count), True, (255, 255, 255))
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (1,50,32), pygame.Rect(0, 0, SCREEN_WIDTH, 100))
        screen.blit(clock_text, (1, 20))
        screen.blit(period_text, (1, 1))
        screen.blit(player_health_text, (1,45))
        screen.blit(player_speed_text, (1,65))
        screen.blit(player_net_text, (SCREEN_WIDTH - 210,1))
        screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
        screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
        screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
        screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
        screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
        screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))
        screen.blit(count_text, (SCREEN_WIDTH/2 - (count_text.get_width()/2), SCREEN_HEIGHT/2))
        player.update(screen)
        if curr_period >= 1:
            enemy.update(screen)
        time_1 = time.time()
        if time_1 - time_0 >= 1: #increments every 'n' seconds
            count -= 1
            time_0 = time_1
        if count <= 0:
            wait = False
        pygame.display.update()
        clock.tick(40)  

period_font = pygame.font.SysFont('goudyoldstyle', 18)
creature_font = pygame.font.SysFont('goudyoldstyle', 20)
def updatePeriod(screen, year):
    global period_text
    global clock_text_color
    global clock_font
    global curr_period
    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text
    global start_period
    ordovician_year_start = 485
    silurian_year_start = 444
    devonian_year_start = 419
    carboniferous_year_start = 359
    permian_year_start = 299
    
    if (year - ordovician_year_start == 5) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - ordovician_year_start == 4) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - ordovician_year_start == 3) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - ordovician_year_start == 2) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - ordovician_year_start == 1) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - silurian_year_start == 5) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - silurian_year_start == 4) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - silurian_year_start == 3) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - silurian_year_start == 2) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - silurian_year_start == 1) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - devonian_year_start == 5) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - devonian_year_start == 4) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - devonian_year_start == 3) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - devonian_year_start == 2) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - devonian_year_start == 1) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - carboniferous_year_start == 5) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - carboniferous_year_start == 4) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - carboniferous_year_start == 3) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - carboniferous_year_start == 2) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - carboniferous_year_start == 1) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - permian_year_start == 5) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - permian_year_start == 4) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - permian_year_start == 3) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - permian_year_start == 2) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - permian_year_start == 1) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)

    if (year == silurian_year_start - 5) or (year == devonian_year_start - 5) or (year == carboniferous_year_start - 5) or (year == permian_year_start - 5):
        buoyObstacle2.set_location()


    if year == ordovician_year_start:
        ordPeriod.display_text(screen, ordPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        curr_period = 1
        print(curr_period)
        pygame.mixer.Sound.play(clock_chime_sound)
        game_paused(False)
        period_text = display_font.render('ORDOVICIAN PERIOD     | NEXT PERIOD: '+str(silurian_year_start)+' MYA |', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == silurian_year_start:
        silPeriod.display_text(screen, silPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        curr_period = 2
        pygame.mixer.Sound.play(clock_chime_sound)
        game_paused(False)
        period_text = display_font.render('SILURIAN PERIOD     | NEXT PERIOD: '+str(devonian_year_start)+' MYA |', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == devonian_year_start:
        devPeriod.display_text(screen, devPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.xpos = -buoyObstacle2.width
        curr_period = 3
        pygame.mixer.Sound.play(clock_chime_sound)
        game_paused(False)
        period_text = display_font.render('DEVONIAN PERIOD     | NEXT PERIOD: '+str(carboniferous_year_start)+' MYA |', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == carboniferous_year_start:
        carPeriod.display_text(screen, carPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.xpos = -buoyObstacle2.width
        curr_period = 4
        pygame.mixer.Sound.play(clock_chime_sound)
        game_paused(False)
        period_text = display_font.render('CARBONIFEROUS PERIOD     | NEXT PERIOD: '+str(permian_year_start)+' MYA |', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == permian_year_start:
        perPeriod.display_text(screen, perPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.xpos = -buoyObstacle2.width
        curr_period = 5
        pygame.mixer.Sound.play(clock_chime_sound)
        game_paused(False)
        period_text = display_font.render('PERMIAN PERIOD     | FINAL PERIOD |', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == 252:
        period_text = 'END'

#GAME MANAGEMENT
game_state = [0, 1, 2]
curr_year = 541
time_0 = time.time()
enemy_direction_time = 0
fish_wait_time = int(random.randint(2, 4))
waiting_for_fish = False

global creatures_found
creatures_found = 0
global creatures_unknown
creatures_unknown = 30

global curr_period
curr_period = 0

unknown_font = pygame.font.SysFont('goudyoldstyle', 17)
global prestige1a_text
global prestige1b_text
global prestige2a_text
global prestige2b_text
global prestige3_text
prestige1a_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
prestige1b_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
prestige2a_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
prestige2b_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
prestige3_text = unknown_font.render('***   _____?_____', True, (255, 255, 255))
def reset_prestige_text():
    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text
    prestige1a_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
    prestige1b_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
    prestige2a_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
    prestige2b_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
    prestige3_text = unknown_font.render('***   _____?_____', True, (255, 255, 255))


clock_text = clock_font.render(str(curr_year) + ' MYA', True, clock_text_color)
player_health_text = display_font.render('HEALTH: ' + str(player.healthbar()), True, (255, 255, 255))
player_speed_text = display_font.render('SPEED: ' + str(player.speedbar()), True, (255, 255, 255))
player_score_text = display_font.render('SCORE: ' + '{:0.1f}'.format(player.score), True, (255, 255, 255))
player_net_text = display_font.render('ANIMALS CAUGHT: ' + str(player.net), True, (255, 255, 255))

new_font = pygame.font.SysFont('goudyoldstyle', 50)
new_creature_found_text = new_font.render('NEW!', True, (139, 0, 0))

global creatures
creatures = [False]*30

def bestiary():
    global creatures
    found = 0
    global creatures_found
    global creatures_unknown
    for x in creatures:
        if x == True:
            found += 1
    creatures_found = found
    creatures_unknown = 30 - found

print(creatures_list[0][0].genus)
print(creatures_list[0][1].genus)
print(creatures_list[0][2].genus)
print(creatures_list[0][3].genus)
print(creatures_list[0][4].genus)
print(creatures_list[1][0].genus)
print(creatures_list[1][1].genus)
print(creatures_list[1][2].genus)
print(creatures_list[1][3].genus)
print(creatures_list[1][4].genus)

water_splash_sound = pygame.mixer.Sound("water_splash.wav")
water_splash_sound.set_volume(0.5)

water_movement_sound = pygame.mixer.Sound("water_movement.wav")
water_movement_sound.set_volume(0.5)

underwater_splash_sound = pygame.mixer.Sound("underwater_splash.wav")
underwater_splash_sound.set_volume(0.5)

clock_chime_sound = pygame.mixer.Sound("chime.wav")
clock_chime_sound.set_volume(0.25)

metal_bang_sound = pygame.mixer.Sound("metal_bang.wav")
metal_bang_sound.set_volume(0.5)

sea_creature_sound = pygame.mixer.Sound('sea_creature.wav')
sea_creature_sound.set_volume(0.75)

crash_wood_sound = pygame.mixer.Sound('crash_wood.wav')
crash_wood_sound.set_volume(0.75)

repair_ship_sound = pygame.mixer.Sound('hammering.wav')
repair_ship_sound.set_volume(0.5)

global ocean_n_ship_pos
ocean_n_ship_pos = 0.0
global play_ocean_sound
play_ocean_sound = True

player_disabled = False

powerup_time = 0

play_metal_bang_sound = True

global start_period
start_period = False

new_game = True
############################## GAME LOOP ##############################
while True:

    current_time = pygame.time.get_ticks()
    player_action = False

    if new_game:
        main_menu()
        pygame.mixer.Sound.play(clock_chime_sound)
        camPeriod.display_text(screen, camPeriod.compile_information(), (10, 10), period_font, (255, 255, 255))
        player.start_pos()
        enemy.start_pos()
        buoyObstacle.set_location()
        print(curr_period)
        game_paused(False)
        count_down()
        new_game = False
    
    if play_ocean_sound:
        pygame.mixer.music.load('ocean_ship.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.25)
        play_ocean_sound = False

    #check if game is paused; else decrement 'curr_year' by 1 per second passed
    if pause == False:
        time_1 = time.time()
        if time_1 - time_0 >= 0.25: #increments every 'n' seconds
            curr_year -= 1
            time_0 = time_1

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (1,50,32), pygame.Rect(0, 0, SCREEN_WIDTH, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.curr_action = 0
                #player.flip = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.curr_action = 0
                #player.flip = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.curr_action = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.curr_action = 0
            if event.key == pygame.K_SPACE and player.canfish == True:
                if player.fishing == False:
                    player.curr_action = 1
                    player.fishing = True
                else:
                    player.curr_action = 0
                    player.fishing = False
            if event.key == pygame.K_p:
                player_action = True
                paused(screen, current_time, player_action)

    # update and dispaly fishing area ripples
    fishArea1.update(screen, current_time)
    fishArea2.update(screen, current_time)
    fishArea3.update(screen, current_time)
    fishArea4.update(screen, current_time)
    fishArea5.update(screen, current_time)

    '''
    oceanWaves.update(screen, current_time)
    oceanWaves2.update(screen, current_time)
    oceanWaves3.update(screen, current_time)
    oceanWaves4.update(screen, current_time)
    oceanWaves5.update(screen, current_time)
    '''


    # every 3 seconds the enemy will either follow the player (hunting speed) or wonder aimlessly (wondering speed)
    if curr_period >= 1:
        if enemy_direction_time + 3000 < current_time:
            enemy.change_direction(player.xpos, player.ypos, player.speed)
            enemy_direction_time = current_time
        enemy.move()
        enemy.update(screen)

    # update and display player movements
    player.handle_keys()
    player.update(screen)

    # display time, player stats, and period
    clock_text = clock_font.render(str(curr_year) + ' MYA', True, clock_text_color)
    clock_text_color = (255, 255, 255)
    clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    player_health_text = display_font.render('HEALTH: ' + str(player.healthbar()), True, (255, 255, 255))
    player_speed_text = display_font.render('SPEED: ' + str(player.speedbar()), True, (255, 255, 255))
    player_score_text = display_font.render('SCORE: ' + '{:0.1f}'.format(player.score), True, (255, 255, 255))
    player_net_text = display_font.render('ANIMALS CAUGHT: ' + str(player.net), True, (255, 255, 255))
    ###creature_found_text = display_font.render('Animals Identified: ' + str(creatures_found), True, (255, 255, 255))
    ###creature_unknown_text = display_font.render('Animals Unknown: ' + str(creatures_unknown), True, (255, 255, 255))
    screen.blit(clock_text, (1, 20))
    updatePeriod(screen, curr_year)
    screen.blit(period_text, (1, 1))

    screen.blit(player_health_text, (1,45))
    screen.blit(player_speed_text, (1,65))
    screen.blit(player_net_text, (SCREEN_WIDTH - 210,1))
    screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
    screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
    screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
    screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
    screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
    screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))
    ###screen.blit(creature_found_text, (SCREEN_WIDTH - 500,1))
    ###screen.blit(creature_unknown_text, (SCREEN_WIDTH - 500,21))

    # create player and fishing area hitboxes and check for collisions while fishing
    player_hitbox = player.actions[player.curr_action].get_rect()
    player_hitbox.topleft = (player.xpos, player.ypos)
    fishArea1Hitbox = fishArea1.actions[fishArea1.curr_action][fishArea1.curr_frame].get_rect()
    fishArea1Hitbox.topleft = (fishArea1.xpos, fishArea1.ypos)
    fishArea2Hitbox = fishArea2.actions[fishArea2.curr_action][fishArea2.curr_frame].get_rect()
    fishArea2Hitbox.topleft = (fishArea2.xpos, fishArea2.ypos)
    fishArea3Hitbox = fishArea3.actions[fishArea3.curr_action][fishArea3.curr_frame].get_rect()
    fishArea3Hitbox.topleft = (fishArea3.xpos, fishArea3.ypos)
    fishArea4Hitbox = fishArea4.actions[fishArea4.curr_action][fishArea4.curr_frame].get_rect()
    fishArea4Hitbox.topleft = (fishArea4.xpos, fishArea4.ypos)
    fishArea5Hitbox = fishArea5.actions[fishArea5.curr_action][fishArea5.curr_frame].get_rect()
    fishArea5Hitbox.topleft = (fishArea5.xpos, fishArea5.ypos)

    if player.fishing == False:
        fish_wait_time = int(random.randint(2, 4))
    if ((pygame.Rect.colliderect(player_hitbox, fishArea1Hitbox) and fishArea1.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea2Hitbox) and fishArea2.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea3Hitbox) and fishArea3.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea4Hitbox) and fishArea4.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea5Hitbox) and fishArea5.active == True)) and player.fishing:
        fish_1 = time.time()
        if waiting_for_fish == False:
            fish_0 = time.time()
            waiting_for_fish = True
        if fish_1 - fish_0 >= 1:
            print('waiting for fish')
            fish_wait_time -= 1
            fish_0 = fish_1
        
        if fish_wait_time <= 0:
            print('fishing')
            creature_val = int(random.randint(0, 4))
            caught_creature = creatures_list[curr_period][creature_val]
            if pygame.Rect.colliderect(player_hitbox, fishArea1Hitbox):
                fishArea1.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea2Hitbox):
                fishArea2.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea3Hitbox):
                fishArea3.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea4Hitbox):
                fishArea4.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea5Hitbox):
                fishArea5.active = False
            caught_creature.generate_size()
            caught_creature.generate_rating()
            caught_creature.display_text(screen, caught_creature.compile_information(), (10, 10), creature_font, (255, 255, 255))
            if creatures[caught_creature.id] == False:
                screen.blit(new_creature_found_text, (SCREEN_WIDTH - 450, 10))
                if creature_val == 0:
                    prestige1a_text = unknown_font.render('*   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 1:
                    prestige1b_text = unknown_font.render('*   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 2:
                    prestige2a_text = unknown_font.render('**   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 3:
                    prestige2b_text = unknown_font.render('**   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 4:
                    prestige3_text = unknown_font.render('***   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
            creatures[caught_creature.id] = True
            bestiary()
            player.net += 1
            player.score += caught_creature.rating_val
            pygame.mixer.Sound.play(water_movement_sound)
            caught_creature.update(screen)
            game_paused(True)
            pygame.mixer.Sound.play(water_splash_sound)
            waiting_for_fish = False
            fish_wait_time = int(random.randint(2, 4))
            player.curr_action = 0
    
    barrel_hitbox = barrelPowerup.img[barrelPowerup.curr_img].get_rect()
    barrel_hitbox.topleft = (barrelPowerup.xpos, barrelPowerup.ypos)
    oar_hitbox = oarPowerup.img[oarPowerup.curr_img].get_rect()
    oar_hitbox.topleft = (oarPowerup.xpos, oarPowerup.ypos)

    buoy_hitbox = buoyObstacle.img[buoyObstacle.curr_img].get_rect()
    buoy_hitbox.topleft = (buoyObstacle.xpos, buoyObstacle.ypos)
    buoy_hitbox2 = buoyObstacle2.img[buoyObstacle2.curr_img].get_rect()
    buoy_hitbox2.topleft = (buoyObstacle2.xpos, buoyObstacle2.ypos)

    enemy_hitbox = enemy.actions[enemy.curr_action].get_rect()
    enemy_hitbox.topleft = (enemy.xpos, enemy.ypos)

    buoy1 = int(random.randint(1,2))
    buoy2 = int(random.randint(1,2))

    buoyobstacle1 = int(random.randint(1,2))
    buoyobstacle2 = int(random.randint(1,2))

    if player_disabled:
        if player_disabled_time + 1500 < current_time:
            player.speed = player.curr_speed
            buoyObstacle.enabled = True
            buoyObstacle2.enabled = True

    if powerup_time + 10000 < current_time:
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        chance = int(random.randint(1,3))
        if chance == 1:
            oarPowerup.enabled = True
            oarPowerup.set_location()
        elif chance == 2:
            barrelPowerup.enabled = True
            barrelPowerup.set_location()
        else:
            pass
        
        powerup_time = current_time

    if pygame.Rect.colliderect(player_hitbox, buoy_hitbox):
        if play_metal_bang_sound:
            pygame.mixer.Sound.play(metal_bang_sound)
        play_metal_bang_sound = False
        player_disabled_time = current_time
        player_disabled = True
        buoyObstacle.hit_player(player)
        buoyObstacle.enabled = False
        player.speed = 0
        if player.curr_speed == 3:
            player.curr_speed = 2

    if pygame.Rect.colliderect(player_hitbox, buoy_hitbox2):
        if play_metal_bang_sound:
            pygame.mixer.Sound.play(metal_bang_sound)
        play_metal_bang_sound = False
        player_disabled_time = current_time
        player_disabled = True
        buoyObstacle2.hit_player(player)
        buoyObstacle2.enabled = False
        player.speed = 0
        if player.curr_speed == 3:
            player.curr_speed = 2

    if not (pygame.Rect.colliderect(player_hitbox, buoy_hitbox) or pygame.Rect.colliderect(player_hitbox, buoy_hitbox)):
        play_metal_bang_sound = True

    if pygame.Rect.colliderect(player_hitbox, barrel_hitbox):
        if play_repair_sound and player.health < 5:
            pygame.mixer.Sound.play(repair_ship_sound)
        barrelPowerup.applyBonus(player)
        play_repair_sound = False
    if barrelPowerup.enabled:
        barrelPowerup.update(current_time, screen, buoy1)

    if not (pygame.Rect.colliderect(player_hitbox, barrel_hitbox)):
        play_repair_sound = True

    if pygame.Rect.colliderect(player_hitbox, oar_hitbox):
        oarPowerup.applyBonus(player)
    if oarPowerup.enabled:
        oarPowerup.update(current_time, screen, buoy2)

    if not (pygame.Rect.colliderect(player_hitbox, enemy_hitbox)):
        play_enemy_sounds = True
            
    if pygame.Rect.colliderect(player_hitbox, enemy_hitbox):
        if play_enemy_sounds:
            pygame.mixer.Sound.play(crash_wood_sound)
            pygame.mixer.Sound.play(sea_creature_sound)
        play_enemy_sounds = False
        enemy.display_text(screen, enemy.compile_information(), (10, 10), creature_font, (255, 255, 255))
        player.start_pos()
        enemy.start_pos()
        enemy.hit_player(player)
        if player.curr_speed == 3:
            player.curr_speed = 2
        game_paused(True)

    
    buoyObstacle.update(current_time, screen, buoyobstacle1)
    if curr_period >= 2:
        buoyObstacle2.update(current_time, screen, buoyobstacle2)

    if player.health <= 0:
        print('GAME OVER')
        pygame.quit()
        sys.exit

    # update game display
    pygame.display.update()
    clock.tick(40) #40 fps