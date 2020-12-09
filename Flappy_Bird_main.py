# Pygame Beispiel
import os, sys, pygame, pygame.locals

# Initialisieren von PyGame
pygame.init()


# Fenster öffnen
screen =pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption('Flapply Dot')

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True



# vogel koordinate_x_y
x = 100
y = 240



# wand_1_x
a1 = 800

# wand_2_x
a2 = 600

# wand_3_x
a3 = 400

# wand_4_x
a4 = 200

# wand_5_x
a5 = 0

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
            y += 1

    # alle Wände immer nach links bewegen
    a1 -= 1
    a2 -= 1
    a3 -= 1
    a4 -= 1
    a5 -= 1
    # wenn Wand aus screen, nach rechts zurück
    if a1 == -50:
        a1 = 640
    if a2 == -50:
        a2 = 640
    if a3 == -50:
        a3 = 640
    if a4 == -50:
        a4 = 640
    if a5 == -50:
        a5 = 640

    tupleAU = pygame.Rect(a1,0,50,150)
    tupleAD = pygame.Rect(a1,300,50,180)

    tupleBU = pygame.Rect(a2, 0, 50, 200)
    tupleBD = pygame.Rect(a2, 300, 50, 200)

    tupleCU = pygame.Rect(a3, 0, 50, 150)
    tupleCD = pygame.Rect(a3, 300, 50, 180)

    tupleDU = pygame.Rect(a4, 0, 50, 150)
    tupleDD = pygame.Rect(a4, 300, 50, 180)

    tupleEU = pygame.Rect(a5, 0, 50, 150)
    tupleED = pygame.Rect(a5, 300, 50, 180)

    # macht ein list, es hat alle tupel
    list_tuple=[tupleAU,tupleAD,tupleBU,tupleBD,tupleCD,tupleCU,tupleDD,tupleDU,tupleED,tupleEU]

    screen.fill((64, 64, 64))  # Dark Gray

    bird = pygame.Rect(x,y,10,10) #get a bird
    pygame.draw.rect(screen, (192, 32, 32), bird)

    pygame.draw.rect(screen,(32,192,32),tupleAU)
    pygame.draw.rect(screen,(32,192,32),tupleAD)
    pygame.draw.rect(screen, (32, 192, 32), tupleBU)
    pygame.draw.rect(screen, (32, 192, 32), tupleBD)
    pygame.draw.rect(screen, (32, 192, 32), tupleCU)
    pygame.draw.rect(screen, (32, 192, 32), tupleCD)
    pygame.draw.rect(screen, (32, 192, 32), tupleDU)
    pygame.draw.rect(screen, (32, 192, 32), tupleDD)
    pygame.draw.rect(screen, (32, 192, 32), tupleEU)
    pygame.draw.rect(screen, (32, 192, 32), tupleED)




# Fenster aktualisieren
    pygame.display.flip()

# if Bird out screen,end game
    if y==480:
        break
        # pygame.quit()


# Refresh-Zeiten festlegen
    clock.tick(60)

# Bestimmen es, ob es kollidieren werden
    for i in list_tuple:
        a = pygame.Rect.colliderect(bird, i)
        # whenn kollidieren enden game
        if a == 1:
            spielaktiv=False

pygame.quit()
