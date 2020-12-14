#Aufgehoben
#
#
#给某些不懂python还要bb的傻逼看的注释
#import some pakcage from pygame
import pygame
#import all funcktion from pygame.locals
from pygame.locals import *
#傻逼太多了，解释不过来

#initizliation pygame
pygame.init()
#set resoultion
#老子换个不常用的分辨率这傻逼总不能说是我抄的吧
screen = pygame.display.set_mode((1922,1088))

#set this variablen to mark when game is runing or not
gameing = True

#main loop for this game
#主循环
while gameing:
    #detect some event
    for event in pygame.event.get():
        #when somebody push the button
        if event.type == KEYDOWN:
            #and the key they push is ESC
            if event.key == K_ESCAPE:
                #stop game
                gameing = False
        #and if someone click the quit button or any other opeartion
        if event.type == pygame.locals.QUIT:
            #stop game
            gameing = False
#跟傻逼解释半天不知道他们能不能看懂

#quti pygame
pygame.quit()