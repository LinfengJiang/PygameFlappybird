import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('testCollsion')
clock = pygame.time.Clock()

gameing = True

m = 300 #use m to control rect2

while gameing:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameing = False
        if event.type == pygame.locals.QUIT:
            gameing = False

    #background color
    screen.fill((255,255,0))

    test_img = pygame.image.load("lighter.png")  #load picture
    test_img = pygame.transform.smoothscale(test_img,[193,48])   #transform the pixel into 193x48

    rect1 = pygame.Rect(0,0,50,50)  #(left,top,width,height)
    rect2 = pygame.Rect(m,0,193,48)

    # rect3 = test_img.get_rect()   #trying

    pygame.draw.rect(screen,(32,192,32),rect1)
    pygame.draw.rect(screen, (255, 255, 255), rect2)
    # pygame.draw.rect(screen,(0,0,0),rect3)
    screen.blit(test_img,rect2)

    a = pygame.Rect.colliderect(rect1,rect2)  #check if rect1 and rect2 collsion

    if a == 1: #when rect1 and rect2 collision
        print("collision")
    if m > 0:
        m = m-1
    else:
        m = 300      #move rect2 from 100 to 0, when 0, move to 100


    pygame.display.flip()
    clock.tick(60)

pygame.quit()