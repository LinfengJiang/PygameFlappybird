# Pygame
import os, sys, pygame, pygame.locals,random

# Initialisieren von PyGame
pygame.init()


# Fenster öffnen
screen = pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Bird')

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Wand Geschwendigkeit
geschwendigkeit = 1

# vogel koordinate_x_y
x = 200
y = 240



# wand_1_x ,jede Wand beginnt von rechts, Abstand 150 ,Wand Breite 50
a1 = 640

# wand_2_x +250
a2 = 840

# wand_3_x
a3 = 1040

# wand_4_x
a4 = 1240

# braucht ein random Lücke,so gibt ein random Wands Lange l
list_l = [80,100,120,140, 160,180,200,220,240,260,280,300, 320]
lA = random.choice(list_l)
lB = random.choice(list_l)
lC = random.choice(list_l)
lD = random.choice(list_l)

# Schleife Hauptprogramm
while spielaktiv:

# Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT or (
                event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE):
            # Spiel wird beendet!
            spielaktiv=False

# Aktualisieren des Zustands
#     if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
#         x -= 1
#     elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
#         x += 1

    # vogel mit jede ein mal K_UP nach oben 10
    if pygame.key.get_pressed()[pygame.locals.K_UP]:
        y -= 10

    # vogel fallen immer
    else :
        if y > 0:
            y += 3
    # alle Wände immer nach links bewegen
    a1 -= geschwendigkeit
    a2 -= geschwendigkeit
    a3 -= geschwendigkeit
    a4 -= geschwendigkeit

    # wenn grans Wand aus screen, nach rechts zurück und gibt es ein neue Lücke
    if a1 == -50:
        a1 = 750
        lA = random.choice(list_l)
    if a2 == -50:
        a2 = 750
        lB = random.choice(list_l)
    if a3 == -50:
        a3 = 750
        lC = random.choice(list_l)
    if a4 == -50:
        a4 = 750
        lD = random.choice(list_l)


    tupleAU = pygame.Rect(a1,0,50,lA)
    tupleAD = pygame.Rect(a1,lA+100,50,380-lA)

    tupleBU = pygame.Rect(a2, 0, 50, lB)
    tupleBD = pygame.Rect(a2, lB+100, 50, 380-lB)

    tupleCU = pygame.Rect(a3, 0, 50, lC)
    tupleCD = pygame.Rect(a3, lC+100, 50, 380-lC)

    tupleDU = pygame.Rect(a4, 0, 50, lD)
    tupleDD = pygame.Rect(a4, lD+100, 50,380-lD)


    # macht ein list, es hat alle tupel
    list_tuple=[tupleAU,tupleAD,tupleBU,tupleBD,tupleCD,tupleCU,tupleDD,tupleDU]

    screen.fill((64, 64, 64))  # Dark Gray

    bird = pygame.Rect(x,y,10,10) #get a bird( Quadrat)
    pygame.draw.rect(screen, (192, 32, 32), bird)

    pygame.draw.rect(screen,(32,192,32),tupleAU)
    pygame.draw.rect(screen,(32,192,32),tupleAD)
    pygame.draw.rect(screen, (32, 192, 32), tupleBU)
    pygame.draw.rect(screen, (32, 192, 32), tupleBD)
    pygame.draw.rect(screen, (32, 192, 32), tupleCU)
    pygame.draw.rect(screen, (32, 192, 32), tupleCD)
    pygame.draw.rect(screen, (32, 192, 32), tupleDU)
    pygame.draw.rect(screen, (32, 192, 32), tupleDD)


# Fenster aktualisieren
    pygame.display.flip()

# if Bird out screen,end game
    if y==480 or y<=0:
        break
        # pygame.quit()


# Refresh-Zeiten festlegen
    clock.tick(60)

# Bestimmen es, ob es kollidieren werden
    for i in list_tuple:
        a = pygame.Rect.colliderect(bird, i)
        # whenn kollidieren enden game
        if a == 1:
            spielaktiv = False

pygame.quit()
