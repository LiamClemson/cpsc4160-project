#IMPORT STATEMENTS
import pygame, sys, os
import time
from models import *
from images import *
import pygame.freetype

"""
NOTES

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

#SPRITE DECLARATION AND INITIALIZATION
player = fisherman()
player.add_images(fisherman_idle_img, fisherman_fishing_img)
fishing_area_1 = ripples()
fishing_area_1.set_location_random()
fishing_area_2 = ripples()
fishing_area_2.set_location_random()
fishing_area_3 = ripples()
fishing_area_3.set_location_random()
enemy = Enemy()
enemy.add_images(shadow_moving1, shadow_moving2, shadow_moving3)

#TEXT SETTINGS
period_font = pygame.font.SysFont('Camrbia', 30)
global period_text
period_text = period_font.render('CAMBRIAN PERIOD', True, (255, 255, 255))
stats_font = pygame.font.SysFont('Camrbia', 25)
global player_health_text
player_health_text = stats_font.render('Health: ' + str(player.health), True, (255, 255, 255))
global player_speed_text
player_speed_text = stats_font.render('Speed: ' + str(player.speed), True, (255, 255, 255))
global player_weapon_text
player_weapon_text = stats_font.render('Weapon: ' + player.weapon, True, (255, 255, 255))
clock_font = pygame.font.SysFont('Camrbia', 30)
clock_text = clock_font.render('0', True, (255, 255, 255))

#TIME SETTINGS
clock_enabled = True

global pause
pause = False
def paused():
    global pause
    pause = True
    pause_font = pygame.font.SysFont('Camrbia', 50)
    pause_text = pause_font.render('PAUSED', True, (255, 255, 255))
    screen.blit(pause_text, (100, 100))

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

def newPeriod(period_name):
    global period_text
    period_text = period_font.render(period_name, True, (139, 0, 0))
    screen.blit(period_text, (1, 1))
    screen.blit(clock_text, (1, 20))
    pygame.display.update()
    time.sleep(2)
    period_text = period_font.render(period_name, True, (255, 255, 255))

def updatePeriod(year):
    global curr_year
    if year == 485:
        newPeriod('ORDOVICIAN PERIOD')
    elif year == 444:
        newPeriod('SILURIAN PERIOD')
    elif year == 419:
        newPeriod('DEVONIAN PERIOD')
    elif year == 359:
        newPeriod('CARBONIFEROUS PERIOD')
    elif year == 299:
        newPeriod('PERMIAN PERIOD')
    elif year == 252:
        newPeriod('END')

#GAME MANAGEMENT
game_state = [0, 1, 2]
curr_year = 541
time_0 = time.time()
enemy_direction_time = 0

############################## GAME LOOP ##############################
while True:

    current_time = pygame.time.get_ticks()

    #check if game is paused; else decrement 'curr_year' by 1 per second passed
    if pause == False:
        time_1 = time.time()
        if time_1 - time_0 >= 1:
            curr_year -= 1
            time_0 = time_1

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (139,0,0), pygame.Rect(0, 0, SCREEN_WIDTH, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.curr_action = 0
                player.flip = False
            if event.key == pygame.K_LEFT:
                player.curr_action = 0
                player.flip = True
            if event.key == pygame.K_UP:
                player.curr_action = 0
            if event.key == pygame.K_DOWN:
                player.curr_action = 0
            if event.key == pygame.K_SPACE and player.canfish == True:
                if player.fishing == False:
                    player.curr_action = 1
                    player.fishing = True
                else:
                    player.curr_action = 0
                    player.fishing = False
            if event.key == pygame.K_p:
                paused()

    screen.blit(fishing_area_1.actions[fishing_area_1.curr_action][fishing_area_1.curr_frame], (fishing_area_1.xpos, fishing_area_1.ypos))
    screen.blit(fishing_area_2.actions[fishing_area_2.curr_action][fishing_area_2.curr_frame], (fishing_area_2.xpos, fishing_area_2.ypos))
    screen.blit(fishing_area_3.actions[fishing_area_3.curr_action][fishing_area_3.curr_frame], (fishing_area_3.xpos, fishing_area_3.ypos))
    fishing_area_1.randomly_ripple(current_time)
    fishing_area_2.randomly_ripple(current_time)
    fishing_area_3.randomly_ripple(current_time)

    #player.draw(screen)
    player.handle_keys()

    # every 3 seconds the enemy sprite has:
    # 50% chance to change direction on the x axis (moving left or right)
    # 33% chance to change direction on the y axis (moving up, down, or neutral)
    if enemy_direction_time + 3000 < current_time:
        enemy.change_direction()
        enemy_direction_time = current_time

    enemy.move()
    if enemy.direction == -1:
        screen.blit(enemy.actions[enemy.curr_action], (enemy.xpos, enemy.ypos))
    if enemy.direction == 1:
        screen.blit((pygame.transform.flip(enemy.actions[enemy.curr_action], True, False).convert_alpha()), (enemy.xpos, enemy.ypos))

    if player.flip == False:
        screen.blit(player.actions[player.curr_action], (player.xpos, player.ypos))
    if player.flip == True:
        screen.blit((pygame.transform.flip(player.actions[player.curr_action], True, False).convert_alpha()), (player.xpos, player.ypos))
    
    clock_text = clock_font.render(str(curr_year) + ' mya', True, (255, 255, 255))
    screen.blit(clock_text, (1, 20))
    updatePeriod(curr_year)
    screen.blit(period_text, (1, 1))
    screen.blit(player_health_text, (1,40))
    screen.blit(player_speed_text, (1,55))
    screen.blit(player_weapon_text, (1,70))

    player_hitbox = player.actions[player.curr_action].get_rect()
    player_hitbox.topleft = (player.xpos, player.ypos)

    fishingarea1_hitbox = fishing_area_1.actions[fishing_area_1.curr_action][fishing_area_1.curr_frame].get_rect()
    fishingarea1_hitbox.topleft = (fishing_area_1.xpos, fishing_area_1.ypos)

    if (pygame.Rect.colliderect(player_hitbox, fishingarea1_hitbox)) and player.fishing:
        print('fishing')

    pygame.display.update()
    clock.tick(40) #40 fps