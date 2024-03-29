import os
import sys

# import some pakcage from pygame
import pygame
# import all funcktion from pygame.locals
from pygame.locals import *

import time


import read_ini

conf = read_ini.conf_speed()

import Mulitplayer.last_score as ls  # this funktion is use to upload the score into database
import Mulitplayer.register as reg  # this funktion is use to register an account into database

# register the ID
try:
    reg.register('test')  # regeister as ID 'test'
except BaseException as e:
    print(e)  # print any error

import random

base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

display_width = 640
display_height = 480
black = ( 0 , 0 , 0 )
WHITE = (255, 255, 255)
RED = (255, 0, 0)
#bg = pygame.image.load("./resource/bg.png")
bg = pygame.image.load(os.path.join(base_path,"./resource/bg.png"))
BJ_img = pygame.image.load(os.path.join(base_path,"./resource/BJ.png"))




# initizliation pygame
pygame.init()
# set resoultion


# Button(object) Quelle: https://zhuanlan.zhihu.com/p/78637310
class Button(object):
    # 输入文字，颜色，x偏移量，y偏移量，额外参数
    #need a button name, color and position as parameter
    def __init__(self, text, color, x=None, y=None, **kwargs):
        #define a surface
        self.surface = font.render(text, True, color)
        #set height and width
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        #when a centered parameter became, set the button in position
        if 'centered_x' in kwargs and kwargs['centered_x']:   #如果有要求在x轴居中显示
            self.x = display_width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['centered_y']:
            self.y = display_height // 2 - self.HEIGHT // 2
        else:
            self.y = y

    #show the buttion
    def display(self):
        screen.blit(self.surface, (self.x, self.y)) #button surface and coordinate

    def check_click(self, position):
        #compare if mouse postion is on the button area
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


def Game_start():     #start screen
    #set two global variablen to modify instead of useing return function
    global gameing  #引入全局变量方便后面修改
    global AGAIN
    screen.blit(BJ_img, (0, 0))   #setting a sceen

    game_title = font.render('Flappy Bird', True, black) # set parameter for the title
    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))  #show title

    # pygame.mixer.init()
    # pygame.mixer.music.load('./resource/dj_remix_tari_ubur_ubur_bikin_enak_untuk_goyang.mp3')
    # pygame.mixer.music.play(-1,0)   #start from 0s and loop

    #create two buttons
    play_button = Button('Play', RED, None, 350, centered_x=True)
    exit_button = Button('Exit', black, None, 400, centered_x=True)

    #show the button and refresh the game
    play_button.display()
    exit_button.display()
    pygame.display.update()

    time.sleep(0.5)  #sleep 1s to avoid when restart game, start screen will be jumped

    while True:

        #if mouse moved onto the button area ,then change the button color
        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', RED, None, 350, centered_x=True)
        else:
            play_button = Button('Play', black, None, 350, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('Exit', black, None, 400, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        #some event function
        for event in pygame.event.get():
            #if become quit, then quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            #if mouse has bin clicked
            if play_button.check_click(pygame.mouse.get_pos()):
                #clicked play,resume
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                #clicked exit, exit game
                gameing = False
                AGAIN = False
                break


def Game_end():    #end screen
    #amost same as start screen
    global score
    global AGAIN
    screen.blit(bg, (0, 0))

    game_title = font.render('you are dead', True, WHITE)
    score_title = font.render('your score is:'+str(score), True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))
    screen.blit(score_title, (display_width // 2 - score_title.get_width() // 2, 200))
    end_button = Button('End', WHITE, None, 350, centered_x=True)
    end_button.display()

    restart_button = Button('Restart Game', WHITE, None, 400, centered_x=True)
    restart_button.display()

    pygame.display.update()

    while True:

        if end_button.check_click(pygame.mouse.get_pos()):
            end_button = Button('End', black, None, 350, centered_x=True)
        else:
            end_button = Button('End', WHITE, None, 350, centered_x=True)

        if restart_button.check_click(pygame.mouse.get_pos()):
            restart_button = Button('Restart Game', black, None, 400, centered_x=True)
        else:
            restart_button = Button('Restart Game', WHITE, None, 400, centered_x=True)



        end_button.display()  #show end button
        restart_button.display()    #show restart button
        pygame.display.update()   #refresh display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if end_button.check_click(pygame.mouse.get_pos()):
                AGAIN=False
                break
            elif restart_button.check_click(pygame.mouse.get_pos()):
                break

def Game_pause():
    #also same as start screen
    global AGAIN
    global gameing  #引入全局变量方便后面修改
    screen.blit(bg, (0, 0))

    game_title = font.render('Pause', True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))

    Resume_button = Button('Resume', RED, None, 350, centered_x=True)
    Quit_button = Button('Quit Game', WHITE, None, 400, centered_x=True)

    Resume_button.display()
    Quit_button.display()

    pygame.display.update()

    while True:

        if Resume_button.check_click(pygame.mouse.get_pos()):
            Resume_button = Button('Resume', RED, None, 350, centered_x=True)
        else:
            Resume_button = Button('Resume', WHITE, None, 350, centered_x=True)

        if Quit_button.check_click(pygame.mouse.get_pos()):
            Quit_button = Button('Quit Game', RED, None, 400, centered_x=True)
        else:
            Quit_button = Button('Quit Game', WHITE, None, 400, centered_x=True)

        Resume_button.display()
        Quit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if Resume_button.check_click(pygame.mouse.get_pos()):
                break
            if Quit_button.check_click(pygame.mouse.get_pos()):
                AGAIN = False
                gameing = False
                break
# Button(object) Quelle: https://zhuanlan.zhihu.com/p/78637310

#set resolution
screen = pygame.display.set_mode((display_width, display_height))
#import background picture
BJ = pygame.image.load(os.path.join(base_path,"./resource/BJ.png"))
#set font type and size
font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Bird')

# 刷新率，或者叫刷新速度  refresh rate
clock = pygame.time.Clock()

AGAIN = True




while AGAIN:

    # set this variablen to mark when game is runing or not




    # Wand Geschwendigkeit
    # 值必须能被50整除
    geschwendigkeit = conf.get('X_speed')  # get first value as wall speed

    # vogel koordinate_x_y
    x = 200
    y = 240

    # Score
    score = 0

    # wand_1_x ,jede Wand beginnt von rechts, Abstand 150 ,Wand Breite 50
    a1 = 640

    # wand_2_x +200
    a2 = 840

    # wand_3_x
    a3 = 1040

    # wand_4_x
    a4 = 1240

    # braucht ein random Lücke,so gibt ein random Wands Lange l
    list_l = [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]
    lA = random.choice(list_l)
    lB = random.choice(list_l)
    lC = random.choice(list_l)
    lD = random.choice(list_l)


    # Initialize the font module.
    pygame.font.init()
    # Create a Font object from a font file.
    myfont = pygame.font.Font(None,60)

    gameing = True
    Game_start()


    # main loop for this game
    # 主循环
    while gameing:
        # detect some event
        for event in pygame.event.get():
            # when somebody push the button
            if event.type == KEYDOWN:
                # and the key they push is ESC
                if event.key == K_ESCAPE:
                    # pause menu
                    Game_pause()
            # and if someone click the quit button or any other opeartion
            if event.type == pygame.locals.QUIT:
                # stop game
                gameing = False


        bird_img = pygame.image.load(os.path.join(base_path,"./resource/bird2.png"))  #load picture
        bird_img = pygame.transform.smoothscale(bird_img,[46,25])   #transform the pixel into 46*25
        BJ_img = pygame.image.load(os.path.join(base_path,"./resource/BJ.png"))
        BJ_img = pygame.transform.smoothscale(BJ_img, [640, 480])

        # vogel mit jede ein mal K_UP nach oben 5()
        if pygame.key.get_pressed()[pygame.locals.K_UP]:
            y -= conf.get('K_up')

        # vogel fallen immer
        else:
            if y > 0:
                y += conf.get('Y_speed')
        # alle Wände immer nach links bewegen
        a1 -= geschwendigkeit
        a2 -= geschwendigkeit
        a3 -= geschwendigkeit
        a4 -= geschwendigkeit

        # wenn grans Wand aus screen, nach rechts zurück und gibt es ein neue Lücke
        if a1 <= -50:
            a1 = 750
            lA = random.choice(list_l)
        if a2 <= -50:
            a2 = 750
            lB = random.choice(list_l)
        if a3 <= -50:
            a3 = 750
            lC = random.choice(list_l)
        if a4 <= -50:
            a4 = 750
            lD = random.choice(list_l)

        # Scoreboard
        # When bird pass the wall,
        # that means the coordinates for the wall is C(brid) - thickness of walls
        if a1 == 150:
            score += 1
        if a2 == 150:
            score += 1
        if a3 == 150:
            score += 1
        if a4 == 150:
            score += 1

        # coordinates for rect
        rectA1 = pygame.Rect(a1, 0, 50, lA)
        rectA2 = pygame.Rect(a1, lA + 100, 50, 380 - lA)

        rectB1 = pygame.Rect(a2, 0, 50, lB)
        rectB2 = pygame.Rect(a2, lB + 100, 50, 380 - lB)

        rectC1 = pygame.Rect(a3, 0, 50, lC)
        rectC2 = pygame.Rect(a3, lC + 100, 50, 380 - lC)

        rectD1 = pygame.Rect(a4, 0, 50, lD)
        rectD2 = pygame.Rect(a4, lD + 100, 50, 380 - lD)

        # macht ein list, es hat alle tupel
        list_tuple = [rectA1, rectA2, rectB1, rectB2, rectC1, rectC2, rectD1, rectD2]


        screen.blit(BJ_img,(0,0))

        bird = pygame.Rect(x, y, 46, 25)  # get a bird( Quadrat)
        screen.blit(bird_img,bird) #draw bird img on rect bird


        wand_img = pygame.image.load(os.path.join(base_path,"./resource/wand.png"))  #load picture
        wandA1_img = pygame.transform.smoothscale(wand_img, [50, lA])
        wandA2_img = pygame.transform.smoothscale(wand_img, [50, 380 - lA])
        wandB1_img = pygame.transform.smoothscale(wand_img, [50, lB])
        wandB2_img = pygame.transform.smoothscale(wand_img, [50, 380 - lB])
        wandC1_img = pygame.transform.smoothscale(wand_img, [50, lC])
        wandC2_img = pygame.transform.smoothscale(wand_img, [50, 380 - lC])
        wandD1_img = pygame.transform.smoothscale(wand_img, [50, lD])
        wandD2_img = pygame.transform.smoothscale(wand_img, [50, 380 - lD])

        screen.blit(wandA1_img, rectA1)
        screen.blit(wandA2_img, rectA2)
        screen.blit(wandB1_img, rectB1)
        screen.blit(wandB2_img, rectB2)
        screen.blit(wandC1_img, rectC1)
        screen.blit(wandC2_img, rectC2)
        screen.blit(wandD1_img, rectD1)
        screen.blit(wandD2_img, rectD2)






        # if Bird out screen,end game, und etwas ausdrüken
        if y > 480 or y <= 0:
            print('Try again')
            gameing = False
            Game_end()
            # pygame.quit()



        # Bestimmen es, ob es kollidieren werden
        for i in list_tuple:
            a = pygame.Rect.colliderect(bird, i)
            # wenn kollidieren enden game
            if a == 1:
                gameing = False
                Game_end()
        textImage = myfont.render("score: " + str(score), True, (0, 0, 255))


        # Draw text on a new Surface object.
        screen.blit(textImage, (10,10))



        # set refresh rate as 60, same as normal screen refresh rate
        clock.tick(60)
        # Fenster aktualisieren
        pygame.display.flip()

    # Wenn end der Spielen , ausdrüken der letzt Punkte
    print('Your score is:', score)
    # upload the score into database
    ls.insert_last_score(score)


# quit pygame
pygame.quit()
