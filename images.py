import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fisherman_idle_img = pygame.image.load('fisherman_idle.png').convert_alpha()
fisherman_fishing_img = pygame.image.load('fisherman_fishing.png').convert_alpha()
raw_shadow_moving1 = pygame.image.load('shadow_in_water_1.png').convert_alpha()
raw_shadow_moving2 = pygame.image.load('shadow_in_water_2.png').convert_alpha()
raw_shadow_moving3 = pygame.image.load('shadow_in_water_3.png').convert_alpha()
shadow_moving1 = pygame.transform.scale(raw_shadow_moving1, (50 * 2, 25 * 2))
shadow_moving2 = pygame.transform.scale(raw_shadow_moving2, (50 * 2, 25 * 2))
shadow_moving3 = pygame.transform.scale(raw_shadow_moving3, (50 * 2, 25 * 2))
ripples_img = pygame.image.load('ripples.png').convert_alpha()
ripples1_img = pygame.image.load('ripples1.png').convert_alpha()
ripples2_img = pygame.image.load('ripples2.png').convert_alpha()
ripples3_img = pygame.image.load('ripples3.png').convert_alpha()
ripples4_img = pygame.image.load('ripples4.png').convert_alpha()
ripples5_img = pygame.image.load('ripples5.png').convert_alpha()
ripples6_img = pygame.image.load('ripples6.png').convert_alpha()
ripples7_img = pygame.image.load('ripples7.png').convert_alpha()
#fisherman_idle_img = pygame.transform.scale(fisherman_idle_img, (50, 25))
#fisherman_fishing_img = pygame.transform.scale(fisherman_fishing_img, (50, 25))