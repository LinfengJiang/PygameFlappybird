
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


display_width = 640
display_height = 480
WHITE = (255, 255, 255)
RED = (255, 0, 0)

bg_location = 'bg.png'





# initizliation pygame
pygame.init()
# set resoultion



class Button(object):
    # 输入文字，颜色，x偏移量，y偏移量，额外参数
    def __init__(self, text, color, x=None, y=None, **kwargs):
        self.surface = font.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:   #如果有要求在x轴居中显示
            self.x = display_width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['centered_y']:
            self.y = display_height // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


def Game_start():     #start screen
    global gameing  #引入全局变量方便后面修改
    screen.blit(start_bgp, (0, 0))   #setting a sceen

    game_title = font.render('Flappy Bird', True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))

    pygame.mixer.init()
    pygame.mixer.music.load('./resource/dj_remix_tari_ubur_ubur_bikin_enak_untuk_goyang.mp3')
    pygame.mixer.music.play(-1,0)   #start from 0s and loop

    play_button = Button('Play', RED, None, 350, centered_x=True)
    exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

    play_button.display()
    exit_button.display()
    pygame.display.update()

    time.sleep(0.5)  #sleep 1s to avoid when restart game, start screen will be jumped

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', RED, None, 350, centered_x=True)
        else:
            play_button = Button('Play', WHITE, None, 350, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('Exit', WHITE, None, 400, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                gameing = False
                pygame.quit()
                break


def Game_end():    #end screen
    global score
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
            end_button = Button('End', RED, None, 350, centered_x=True)
        else:
            end_button = Button('End', WHITE, None, 350, centered_x=True)

        if restart_button.check_click(pygame.mouse.get_pos()):
            restart_button = Button('Restart Game', RED, None, 400, centered_x=True)
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
                break
            elif restart_button.check_click(pygame.mouse.get_pos()):
                return 1

def Game_pause():
    global gameing  #引入全局变量方便后面修改
    screen.blit(bg, (0, 0))

    game_title = font.render('Pause', True, WHITE)

    screen.blit(game_title, (display_width // 2 - game_title.get_width() // 2, 150))

    play_button = Button('Resume', RED, None, 350, centered_x=True)
    exit_button = Button('Quit Game', WHITE, None, 400, centered_x=True)

    play_button.display()
    exit_button.display()

    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Resume', RED, None, 350, centered_x=True)
        else:
            play_button = Button('Resume', WHITE, None, 350, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Quit Game', RED, None, 400, centered_x=True)
        else:
            exit_button = Button('Quit Game', WHITE, None, 400, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                break
            if exit_button.check_click(pygame.mouse.get_pos()):
                #pygame.quit()
                gameing = False
                break


screen = pygame.display.set_mode((display_width, display_height))

bg = pygame.image.load(bg_location)
start_bgp = pygame.image.load('./resource/indhome.jpg')
start_bgp = pygame.transform.scale(start_bgp,(640,480))

font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Bird')

# 刷新率，或者叫刷新速度  refresh rate
clock = pygame.time.Clock()




while 1:

    # set this variablen to mark when game is runing or not
    #gameing = True

    end_game = 0

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

    Game_start()
    gameing = True

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


        bird_img = pygame.image.load("./resource/bird2.png")  #load picture
        bird_img = pygame.transform.smoothscale(bird_img,[46,25])   #transform the pixel into 46*25
        BJ_img = pygame.image.load("./resource/BJ.png")
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

        screen.fill((64, 64, 64))  # Dark Gray
        screen.blit(BJ_img,(0,0))

        bird = pygame.Rect(x, y, 46, 25)  # get a bird( Quadrat)
        screen.blit(bird_img,bird) #draw bird img on rect bird


        wand_img = pygame.image.load("./resource/wand.png")  #load picture
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
            # pygame.quit()



        # Bestimmen es, ob es kollidieren werden
        for i in list_tuple:
            a = pygame.Rect.colliderect(bird, i)
            # wenn kollidieren enden game
            if a == 1:
                gameing = False
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

    end_game = Game_end()
    if end_game == 1:
        #gameing = True
        continue
    else:
        break


# quit pygame
pygame.quit()
