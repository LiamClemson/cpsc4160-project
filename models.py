import pygame
import random
from images import *

#CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0, 51, 102)
PURPLE = (230,230,250)

class fisherman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.width = 50
        self.height = 25
        self.xpos = 0
        self.ypos = SCREEN_HEIGHT - self.height

        self.speed = 2
        self.health = 100
        self.weapon = 'harpoon'

        #OTHER VARIABLES
        self.fishing = False
        self.canfish = True

        #ANIMATION VARIABLES
        self.actions = []
        self.curr_action = 0
        self.flip = False

    #FUNC: sets images
    def add_images(self, idle, fishing): #(self, spritesheet)
        self.actions.append(idle)
        self.actions.append(fishing)

    # EDIT RECT STUFF
    #FUNC: handles player movement
    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.xpos < (SCREEN_WIDTH - self.width):
            #self.rect.move_ip(self.speed, 0)
            #self.xpos = self.rect.x
            self.xpos += self.speed
            self.canfish = False
        elif keys[pygame.K_LEFT] and self.xpos > 0:
            #self.rect.move_ip(-self.speed, 0)
            #self.xpos = self.rect.x
            self.xpos -= self.speed
            self.canfish = False
        elif keys[pygame.K_UP] and self.ypos > 105: #100 length of menu block rect
            #self.rect.move_ip(0, -self.speed)
            #self.ypos = self.rect.y
            self.ypos -= self.speed
            self.canfish = False
        elif keys[pygame.K_DOWN] and self.ypos < (SCREEN_HEIGHT - self.height):
            #self.rect.move_ip(0, self.speed)
            #self.ypos = self.rect.y
            self.ypos += self.speed
            self.canfish = False
        else:
            self.canfish = True
############################## END fisherman CLASS ##############################

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.width = 100
        self.height = 50
        self.xpos = SCREEN_WIDTH/2
        self.ypos = SCREEN_HEIGHT/2
        self.direction = -1
        self.moving_up = False
        self.moving_down = True

        self.speed = 2

        #ANIMATION VARIABLES
        self.actions = []
        self.curr_action = 0
        self.flip = False

    #FUNC: sets images
    def add_images(self, moving1, moving2, moving3): #(self, spritesheet)
        self.actions.append(moving1)
        self.actions.append(moving2)
        self.actions.append(moving3)

    #FUNC: move enemy
    def move(self):
        self.xpos += (self.speed)*self.direction
        if self.moving_up:
            self.ypos -= 1
        elif self.moving_down:
            self.ypos += 1
        self.curr_action += 1
        if self.curr_action > 2:
            self.curr_action = 0
        
        
        #CHECK X BOUNDS
        if self.xpos < 0:
            #self.xpos = SCREEN_WIDTH
            self.direction = 1
        elif self.xpos + self.width > SCREEN_WIDTH:
            #self.xpos = 0
            self.direction = -1
        #CHECK Y BOUNDS
        if self.ypos < 100:
            #self.ypos = SCREEN_HEIGHT
            self.moving_up = False
            self.moving_down = True
        elif self.ypos + self.height > SCREEN_HEIGHT:
            #self.ypos = 100
            self.moving_up = True
            self.moving_down = False
        
    def change_direction(self):
        left_right_chance = int(random.randint(0, 1))
        up_down_chance = int(random.randint(0, 2))
        if left_right_chance == 0:
            self.direction*=-1
        if up_down_chance == 0:
            self.moving_up = False
            self.moving_down = False
        elif up_down_chance == 1:
            self.moving_up = True
            self.moving_down = False
        elif up_down_chance == 2:
            self.moving_up = False
            self.moving_down = True
############################## END enemy CLASS ##############################

class ripples(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.active = False
        self.width = 30
        self.height = 30
        self.xpos = 0
        self.ypos = 0
        #time between ripples (RANDOM)
        self.wait_time = 250
        #time the last ripple occured
        self.last_ripple = 0
        self.lifespan = 6000
        #time before the ripple location is changed (SET, 12 seconds)
        self.move_ripple_threshold = self.lifespan

        #ANIMATION VARIABLES
        self.actions = [[ripples_img,ripples1_img,ripples2_img,ripples3_img,ripples4_img,
                        ripples5_img,ripples6_img,ripples7_img]]
        self.curr_action = 0
        self.curr_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.cooldown = 100
        self.step = 0

    #FUNC: sets random wait time between ripples
    #def new_wait_time(self):
    #    self.wait_time = (int(random.randint(0, 3)))*1000
    
    #FUNC: sets animation
    #def add_images(self, ripple, ripple1, ripple2, ripple3, ripple4, ripple5, ripple6, ripple7):
    #    tmp_img = [ripple, ripple1, ripple2, ripple3, ripple4, ripple5, ripple6, ripple7]
    #    self.actions.append(tmp_img)

    #FUNC: sets new coordinates
    def set_location(self, new_x, new_y):
        self.xpos = new_x
        self.ypos = new_y
    
    #FUNC: sets new randomized coordinates
    def set_location_random(self):
        self.xpos = int(random.randint(0, SCREEN_WIDTH - self.width))
        self.ypos = int(random.randint((100 + self.height), SCREEN_HEIGHT - self.height))

    def randomly_ripple(self, current_time):
        if self.move_ripple_threshold - current_time <= 0:
            self.set_location_random()
            self.move_ripple_threshold = current_time + self.lifespan
        if current_time - self.last_ripple >= self.wait_time:
            if current_time - self.last_update >= self.cooldown:
                self.curr_frame += 1
                self.last_update = current_time
                if self.curr_frame >= len(self.actions[self.curr_action]):
                    self.curr_frame = 0
                    self.last_ripple = current_time
                    #self.new_wait_time()
############################## END ripples CLASS ##############################

class land(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.width = 0
        self.height = 0
        self.xpos = 0
        self.ypos = 0
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

        #BODY AND COLLISION VARIABLES
        self.hitbox = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    #FUNC: sets an image to the sprite rect
    def add_img(self, img):
        self.rect = img.get_rect()
        self.land_img = img

    #FUNC: sets new coordinates
    def set_location(self, new_x, new_y):
        self.xpos = new_x
        self.ypos = new_y
    
    #FUNC: sets new size
    def set_size(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    #FUNC: draws/blits the sprite rect on the screen
    def draw(self, screen):
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.hitbox.center = self.rect.center
        pygame.draw.rect(screen, BACKGROUND_COLOR, self.hitbox)
        screen.blit(self.land_img, self.rect)
############################## END land CLASS ##############################

class animal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 0
        self.height = 0
        self.xpos = 0
        self.ypos = 0
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

############################## END animal CLASS ##############################


class period(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 0
        self.height = 0
        self.xpos = (SCREEN_WIDTH / 2) - self.width
        self.ypos = (SCREEN_HEIGHT / 2) - self.height
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

############################## END period CLASS ##############################