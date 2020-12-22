# 给某些不懂python还要bb的傻逼看的注释
# import some pakcage from pygame
import pygame
# import all funcktion from pygame.locals
from pygame.locals import *
# 傻逼太多了，解释不过来

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

# initizliation pygame
pygame.init()
# set resoultion
screen = pygame.display.set_mode((640, 480))

# 刷新率，或者叫刷新速度  refresh rate
clock = pygame.time.Clock()

# set this variablen to mark when game is runing or not
gameing = True

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



pygame.font.init()
myfont = pygame.font.Font(None,60)




# main loop for this game
# 主循环
while gameing:
    # detect some event
    for event in pygame.event.get():
        # when somebody push the button
        if event.type == KEYDOWN:
            # and the key they push is ESC
            if event.key == K_ESCAPE:
                # stop game
                gameing = False
        # and if someone click the quit button or any other opeartion
        if event.type == pygame.locals.QUIT:
            # stop game
            gameing = False
    # 跟傻逼解释半天不知道他们能不能看懂

    # vogel mit jede ein mal K_UP nach oben 10
    if pygame.key.get_pressed()[pygame.locals.K_UP]:
        # 调整上升速度
        y -= conf.get('K_up')  # 10 ist zu Schwier ,testing....

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

    bird = pygame.Rect(x, y, 10, 10)  # get a bird( Quadrat)
    pygame.draw.rect(screen, (192, 32, 32), bird)

    pygame.draw.rect(screen, (32, 192, 32), rectA1)
    pygame.draw.rect(screen, (32, 192, 32), rectA2)
    pygame.draw.rect(screen, (32, 192, 32), rectB1)
    pygame.draw.rect(screen, (32, 192, 32), rectB2)
    pygame.draw.rect(screen, (32, 192, 32), rectC1)
    pygame.draw.rect(screen, (32, 192, 32), rectC2)
    pygame.draw.rect(screen, (32, 192, 32), rectD1)
    pygame.draw.rect(screen, (32, 192, 32), rectD2)

    # Fenster aktualisieren
    pygame.display.flip()

    # if Bird out screen,end game, und etwas ausdrüken
    if y > 480 or y <= 0:
        print('Try again')
        gameing = False
        # pygame.quit()

    # set refresh rate as 60, same as normal screen refresh rate
    clock.tick(60)

    # Bestimmen es, ob es kollidieren werden
    for i in list_tuple:
        a = pygame.Rect.colliderect(bird, i)
        # wenn kollidieren enden game
        if a == 1:
            print('100G!! Overload!!!!')
            gameing = False




    textImage = myfont.render("score: " + str(score), True, (0, 0, 255))
    screen.blit(textImage, (10,10))
    pygame.display.update()
    pygame.time.delay(50)



# Wenn end der Spielen , ausdrüken der letzt Punkte
print('Your score is:', score)
# upload the score into database
ls.insert_last_score(score)

# quit pygame
pygame.quit()
